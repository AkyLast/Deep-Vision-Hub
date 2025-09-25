# 🔥 Detection Fire – Monitoramento Inteligente de Incêndios com YOLOv8 + OpenCV  

O **Detection Fire** é um sistema de **detecção automática de focos de incêndio em vídeo** desenvolvido com **Python, OpenCV, YOLOv8 e CVZone**.  
O objetivo é identificar, em tempo real, regiões de fogo, calcular sua proporção em relação à cena e emitir alertas caso o fogo esteja **descontrolado** (ocupando mais de 5% da área do frame).  

Este projeto une **Visão Computacional Clássica (OpenCV)** e **Deep Learning (YOLOv8)** para oferecer um pipeline **preciso, robusto e escalável**, mostrando como IA pode ser aplicada em **monitoramento crítico e prevenção de desastres**.  

---

## ✨ Principais Funcionalidades
- 📹 **Leitura de vídeo** em tempo real (ou arquivos pré-gravados).  
- 🤖 **Inferência com YOLOv8** usando um modelo customizado (`best.pt`) treinado especificamente para **detecção de fogo**.  
- 🖼️ **Processamento de bounding boxes**:
  - Desenho de caixas delimitadoras em torno das áreas detectadas.  
  - Cálculo da área do fogo em pixels.  
  - Exibição da **proporção (%) do frame em chamas**.  
- 🚨 **Sistema de Alerta Inteligente**:
  - Se a proporção do fogo ultrapassa **5% da cena**, é exibido um alerta visual destacado em vermelho:  
    **“Alerta! Fogo Descontrolado”**.  
- 🎨 **Visualização Avançada com CVZone** para legendas retangulares e alertas bem destacados.

---

## 📂 Estrutura do Repositório
```

detection-fire/
│── Sources/
│   ├── video1.mp4          # Vídeo de teste 1
│   ├── video2.mp4          # Vídeo de teste 2 (default)
│   ├── video3.mp4          # Vídeo de teste 3
│   └── best.pt             # Modelo YOLOv8 treinado para detectar fogo
│── main.py                 # Código principal de execução do sistema

```

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.10+**
- **OpenCV** → leitura e manipulação de vídeo.
- **YOLOv8 (Ultralytics)** → detecção de fogo com rede neural de última geração.
- **CVZone** → visualização de caixas e textos estilizados.
- **NumPy** → manipulação de coordenadas e cálculos.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/AkyLast/deep-vision-hub.git
   cd detection-fire
    ```

2. **Crie e ative um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
    ```

3. **Instale as dependências**

   ```bash
    pip install -r requirements.txt

    # ou

    pip install ultralytics opencv-python cvzone numpy
   ```

4. **Execute o sistema**

   ```bash
   python main.py
   ```

5. **Controles**

   * O vídeo será exibido na janela `Monitoring`.
   * Pressione **Q** para encerrar a execução.

---

## 📖 Como Funciona o Algoritmo

1. **Entrada de Dados**

   * O sistema recebe um vídeo (`video1`, `video2`, `video3`) ou pode ser facilmente adaptado para **câmeras em tempo real (CCTV/IP)**.

2. **Inferência com YOLOv8**

   * O modelo `best.pt`, treinado para fogo, detecta regiões em chamas no frame.
   * Cada detecção retorna uma **bounding box** (x1, y1, x2, y2).

3. **Cálculo da Área**

   * A área do fogo é calculada:

     $$
     área = (x2 - x1) \times (y2 - y1)
     $$
   * Em seguida, é normalizada pela área total do frame (1280 × 720):

     $$
     proporção = \frac{área}{1280 \times 720}
     $$

4. **Classificação de Risco**

   * 🔵 **Seguro**: fogo ocupa < 5% da cena → bounding box azul.
   * 🔴 **Perigo**: fogo ocupa ≥ 5% da cena → bounding box vermelha + alerta “Fogo Descontrolado”.

5. **Saída Visual**

   * Janelas com:

     * Vídeo original + caixas e porcentagem.
     * Mensagem de alerta em destaque se risco for identificado.

---

## 🖼️ Demonstração Visual

* **Fogo controlado (baixo risco)**
  Caixa azul + porcentagem exibida.

* **Fogo descontrolado (alto risco)**
  Caixa vermelha + alerta em destaque:
  **“Alerta! Fogo Descontrolado”**.

*(Imagens e GIFs podem ser adicionados aqui para portfólio)*

---

## 💡 Possíveis Aplicações

* 🌲 **Monitoramento florestal** → prevenção de queimadas.
* 🏭 **Indústrias** → segurança em áreas inflamáveis.
* 🏙️ **Cidades inteligentes** → detecção de incêndios urbanos em tempo real.
* 🚒 **Apoio a bombeiros** → priorização de áreas de risco.

---

## 🔮 Melhorias Futuras

* Adaptação para **streams em tempo real** via RTSP/HTTP.
* Integração com **sistemas de notificação automática** (SMS, e-mail, Telegram).
* Otimização para **IoT/Edge Computing**, rodando em dispositivos embarcados (Jetson Nano, Raspberry Pi).
* Uso de **Modelos multi-classe** para detectar também fumaça e explosões.

---

## 📜 Licença

Projeto aberto para fins acadêmicos e demonstração.
Sinta-se livre para usar como base em pesquisas e aplicações de **IA aplicada à segurança**.

---

## 👤 Autor

**Aky Last**
🔗 [GitHub](https://github.com/AkyLast)
💼 Especialista em **Visão Computacional e Inteligência Artificial**

