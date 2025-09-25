# 🚗 Vision Cars Parking – Detecção de Vagas Ocupadas e Livres com OpenCV

O **Vision Cars Parking** é um projeto de **Visão Computacional** que identifica, em tempo real, se uma vaga de estacionamento está **ocupada** ou **livre** a partir de um vídeo.  
Utilizando **Python + OpenCV**, o sistema processa cada frame, analisa regiões específicas (as vagas) e desenha bordas **verdes** (livre) ou **vermelhas** (ocupada), além de exibir a contagem de pixels brancos processados.

---

## ✨ Destaques do Projeto
- 🟩 **Detecção visual em tempo real** de vagas livres ou ocupadas.  
- 🔎 **Processamento de imagem** com técnicas de:
  - Conversão para escala de cinza.
  - **Limiarização adaptativa** (Adaptive Threshold).
  - **Dilatação morfológica** para destacar regiões.  
- 🧮 **Contagem de pixels não nulos** para classificar ocupação da vaga.  
- 📊 Interface visual com:
  - Retângulos em torno das vagas.  
  - Contador de pixels dentro de cada região.  
- 📂 Modularização em classe `AnalyzeSpace`, responsável pela análise individual de cada vaga.

---

## 📂 Estrutura do Repositório
```

vision-cars-parking/
│── Sources/
│   └── parking.mp4      # Vídeo de exemplo utilizado pelo sistema
│── main.py              # Código principal de processamento e análise

````

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.10+**
- **OpenCV (cv2)** → Processamento de imagens e vídeo.
- **NumPy** → Manipulação de matrizes e kernel de operações.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/AkyLast/deep-vision-hub
   cd vision-cars-parking
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**

   ```bash
    pip install -r vision-cars-parking/requirements.txt

    # ou
    
    pip install opencv-python numpy
   ```

4. **Execute o projeto**

   ```bash
   python main.py
   ```

5. **Controles**

   * O vídeo abrirá em duas janelas:

     * `Running Parking` → com as vagas destacadas.
     * `Image Gray` → imagem processada em escala binária.
   * Pressione **Q** para encerrar a execução.

---

## 📖 Como Funciona

1. O vídeo é carregado e convertido para **escala de cinza**.
2. É aplicado o **limiar adaptativo** para separar áreas claras/escuras.
3. Um **kernel morfológico (2x2)** é usado para dilatar as regiões e aumentar contraste.
4. Cada vaga é definida por coordenadas iniciais (x, y) + altura/largura.
5. Para cada vaga:

   * Conta-se a quantidade de pixels brancos.
   * Se a contagem ultrapassa o **threshold** (`5000`), a vaga é marcada como **ocupada** (vermelho).
   * Caso contrário, como **livre** (verde).
6. O sistema escreve a contagem de pixels dentro de cada vaga.

---

## 🖼️ Exemplo Visual

Durante a execução, você verá algo como:

* Vagas livres → **Bordas verdes**
* Vagas ocupadas → **Bordas vermelhas**
* Contagem de pixels → número branco sobre cada vaga

*(Exemplo ilustrativo: capturas de tela podem ser adicionadas aqui no repositório)*

---

## 💡 Possíveis Melhorias Futuras

* Ajuste dinâmico do **threshold** para diferentes condições de iluminação.
* Integração com **câmeras IP em tempo real**.
* Exportar estatísticas de ocupação para **dashboards web**.
* Uso de **Deep Learning (YOLO, Faster R-CNN)** para detectar veículos sem necessidade de marcação manual das vagas.

---

## 📜 Licença

Este projeto é de uso livre para fins de estudo e demonstração.
Sinta-se à vontade para adaptar, melhorar e utilizar como portfólio.

---

## 👤 Autor

**Aky Last**
🔗 [GitHub](https://github.com/AkyLast)
💼 Foco em **Visão Computacional & Inteligência Artificial**
