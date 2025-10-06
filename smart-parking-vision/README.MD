# 🚗 Smart Parking Vision

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![Python](https://img.shields.io/badge/python-3.10-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## TL;DR

Sistema de visão computacional que detecta ocupação de vagas em vídeos usando ROIs (Regiões de Interesse). Realiza pré-processamento, conta pixels brancos por ROI e sincroniza estados com uma API REST local. Feito para demonstrar competências práticas em OpenCV, integração cliente/servidor e engenharia de dados.

---

## 📑 Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Demonstração](#demonstração)
3. [Arquitetura](#arquitetura)
4. [Tecnologias](#tecnologias)
5. [Configuração (`config.json`)](#configuração-configjson)
6. [Configuração (`main.py`)](#configuração-mainpy)
6. [Execução](#execução)
7. [Como funciona (técnico)](#como-funciona-técnico)
8. [Exemplos de Código](#exemplos-de-código)
9. [Logs e Persistência](#logs-e-persistência)
10. [Revisões / Bugs encontrados & Correções sugeridas](#revisões--bugs-encontrados--correções-sugeridas)
11. [Melhorias sugeridas / Roadmap](#melhorias-sugeridas--roadmap)
12. [Contribuição](#contribuição)
13. [Licença](#licença)
14. [Contato](#contato)

---

## Sobre o Projeto

**Problema:** monitoramento de vagas em estacionamentos/condomínios usando câmeras existentes.

**Solução:** processamento de vídeo por ROI para determinar ocupação e sincronizar com API local. Projeto pensado para demonstrar habilidades técnicas valorizadas por recrutadores: OpenCV, Python, integração REST, manipulação de configs, logging e estrutura de projeto.

**Finalidade:** este sistema não é apenas uma demonstração técnica, mas uma solução estratégica para quem busca transformar a gestão de estacionamentos em um processo **mais inteligente, eficiente e lucrativo**. Com ele, é possível utilizar câmeras já existentes, eliminando altos custos de hardware, e obter em tempo real o status das vagas disponíveis. Isso permite desde a **redução de filas e aumento da satisfação dos clientes**, até a **otimização da ocupação e geração de insights valiosos para decisões de negócio**. Em condomínios, shoppings ou empresas, o diferencial está na **automatização acessível**, que agrega valor imediato sem demandar grandes mudanças na infraestrutura atual.

---

## Demonstração

![demo](Sources/output.gif)


---

## Arquitetura (resumo)

* **main.py** — cliente de processamento de vídeo: carrega `config.json`, pré-processa frames, avalia ROIs (classe `AnalyzeSpace`) e atualiza API.
* **server/app.py** — API Flask: endpoints para criar vagas, retornar status e atualizar vagas.
* **models/roi_analyzer.py** — lógica de contagem, desenho e debounce (`StatusRois`, `AnalyzeSpace`).
* **utils/** — `connection.py` (integração com API), `save_logs.py` (salva logs em Excel).
* **config.json** — centraliza vídeos, ROIs, parâmetros de dilate e área de contagem.

Fluxo: Vídeo → pré-processamento → contagem por ROI → debounce → PATCH API → logs.

---

## Tecnologias

* Python 3.13 (recomendado)
* OpenCV (`opencv-python`)
* NumPy
* Flask
* Requests
* Pandas + openpyxl (logs Excel)

---

## Configuração (`config.json`)
Onde está 0 ou 1 é para disativar ou ativar determinadas funções.

Arquivo central que contém:

* `status_server` — Status para o processamento ser interno(0) ou no servidor(1).
* `videos_config.video_colored.video_path` — lista de paths dos vídeos (ex.: `"Sources/shoppingPark.mp4"` ou `0`, `1`, ... para expecificar a entrada de vídeo do seu computador).
* `rois` — dicionário por estacionamento com listas de ROIs: `{ "id_roi", "x","y","w","h","threshold" }`.
* `dilate` — `kernel` e `iterations` por estacionamento.
* `counting_area_config` — local do placar/contador na imagem.
* `logs_path` — caminho do arquivo Excel para logs.

**Atenção:** Paths no JSON são relativos à raiz do projeto. Ajuste caso execute de outra pasta.

---

## Configuração (`main.py`)
No tocante, as contastes não precisam se preocupar com as aterações, apenas com a diferencial da variável `VIDEOS_PATH`. Teremos que adicionar o índice do vídeo/entrada de vídeos na qual queremos acessar.

A Variável `VIDEOS_PATH` está intriscicamente ligada com o objeto "videos_config" do `.json`, em expecífico, diretamente ligada com o `"video_path`

```json
"videos_config": {
        "video_colored": {"video_path": ["Sources/condPark.mp4", "Sources/shoppingPark.mp4", 0], "size": [1280, 720], "statusDraw_Counter": 1, "statusDraw_idVaga": 1},
        "video_grayscaled": {"status": 0, "size": [550, 360]}
    }
``` 

Exemplo:
```python
   VIDEOS_PATH = VIDEOS_CONFIG["video_colored"]["video_path"][0]  # Primeira variável do "video_path" no .json -> "Sources/condPark.mp4"
   VIDEOS_PATH = VIDEOS_CONFIG["video_colored"]["video_path"][1]  # Segunda variável do "video_path" no .json -> "Sources/shoppingPark.mp4"
   VIDEOS_PATH = VIDEOS_CONFIG["video_colored"]["video_path"][2]  # Terceira variável do "video_path" no .json -> "0", Câmera do computador
```
---

## Execução

1. Inicie a API (servidor local):

```bash
python server/app.py
# padrão: http://127.0.0.1:5000
```

2. Em outro terminal, execute o processamento:

```bash
python main.py
```

* Pressione `q` enquanto a janela do OpenCV estiver em foco para interromper.
* `main.py` chama `utils.connection.set_parking` ao iniciar para registrar as vagas no servidor.

---

## Como funciona (técnico)

1. **Leitura de frame**: `cv2.VideoCapture` → `ret, img`.
2. **Pré-processamento**:

   * `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` (recomendado)
   * `cv2.GaussianBlur` para reduzir ruído
   * `cv2.adaptiveThreshold(..., cv2.THRESH_BINARY_INV, ...)`
   * `cv2.dilate` com `kernel` configurado
3. **Para cada ROI**:

   * recorta região: `frame[y:y+h, x:x+w]`
   * `cv2.countNonZero` para contar pixels brancos
   * compara com `threshold` definido no JSON
   * usa `StatusRois` para debounce (limiter de N frames antes de confirmar mudança)
4. **Desenho**: retângulos coloridos (verde/laranja/vermelho), contadores e ID da vaga.
5. **Sincronização**: quando o estado é confirmado, chama `PATCH /parking/<parking>/<id>` para atualizar o status no servidor.
6. **Logs**: `utils/save_logs.py` escreve eventos em Excel (`Sources/dados.xlsx`).

---

## Exemplos de Código (trechos retirados do projeto)

Trecho de pré-processamento em `main.py`:

```python
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gaussian_gray = cv2.GaussianBlur(img_gray, (9, 9), 1)
img_th = cv2.adaptiveThreshold(
    gaussian_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 12
)
kernel = np.ones(DILATE["kernel"], dtype=np.uint8)
imgDil = cv2.dilate(img_th, kernel, iterations=DILATE["iterations"])
```

Contagem por ROI (`models/roi_analyzer.py`):

```python
def count_white(self):
    cutted = self.frame[self.y: self.y + self.h, self.x: self.x + self.w]
    count = cv2.countNonZero(cutted)
    return count
```

Debounce simplificado (`StatusRois.analyze_roi`):

```python
def analyze_roi(self, new_status=False):
    status_update = self.status
    if self.status != new_status:
        self.limiter -= 1
        if self.limiter == 0:
            self.limiter = 5
            status_update = new_status
            update_parking(parking=self.parking, vaga_id=self.id_roi, status=status_update)
            self.status = status_update
    else:
        self.limiter = 5
    return status_update
```

---

## Logs e Persistência

* Logs são armazenados em Excel conforme `config.json["logs_path"]` (ex.: `Sources/dados.xlsx`). Simulando situações que o uso do banco de dados seja inacessível.
* `utils/save_logs.py` cria o arquivo caso não exista e registra linhas com: `DATA`, `ID_VAGA`, `ESTACIONAMENTO`, `STATUS`.

---

## Melhorias futuras / Roadmap

* **Processamento no servidor**: mover a etapa de verificação das vagas para o servidor, enviando apenas os resultados para os clientes. Isso reduz a carga em máquinas com pouco poder de processamento.
* **Modelos de Deep Learning**: implementação e comparação de dois modelos para detecção de ocupação — um baseado em **PyTorch** e outro em **YOLO**, visando robustez e flexibilidade em diferentes cenários.
* **Armazenamento de imagens em banco de dados**: salvar recortes de vagas e frames relevantes para criar um histórico visual, permitindo análises posteriores e alimentando pipelines de melhoria contínua dos modelos.
* **Treinamento contínuo**: usar o banco de imagens coletado para refinar os modelos, adaptando o sistema a diferentes ambientes (iluminação, clima, ângulos de câmera).
* Dashboard web em tempo real (WebSocket) mostrando vagas.
* Persistência em banco + autenticação na API.
* Testes unitários (mocks para `update_parking`) e CI.
* Dockerfile + Compose (API + processor) para facilitar deploy.

---

## Contribuição

1. Fork → clone → branch `feature/main`
2. Commit claros e descritivos
3. PR com descrição, screenshots e, quando possível, testes

---

## Licença

Este projeto usa **MIT License**. Veja `LICENSE` no repositório.

---

## Contato

* LinkedIn: [Luis Fernando Ribeiro Curvelo](https://www.linkedin.com/in/luis-fernando-ribeiro-curvelo/)
* Email: [luisribeiro.curvelo@gmail.com](mailto:luisribeiro.curvelo@gmail.com)

---
