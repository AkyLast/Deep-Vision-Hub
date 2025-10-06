# 🧠 Deep Vision Hub

Este repositório é um hub pessoal de projetos e estudos em **Visão Computacional**, onde exploro desde técnicas clássicas com OpenCV até aplicações modernas com redes neurais profundas.

---

## 🎯 Propósito

Organizar e documentar o meu progresso em projetos práticos de visão computacional, com foco em:

- Processamento e análise de imagens
- Detecção e contagem de objetos e pessoas
- Integração com modelos de deep learning
- Aplicações reais e escaláveis para visão computacional

---

## 📁 Projetos Incluídos

| Projeto                        | Descrição                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------|
| `vision-people-counting`      | Sistema de contagem de pessoas em vídeos, utilizando processamento de imagem com OpenCV.    |
| `smart-parking-vision`        | Sistema de detecção de ocupação de vagas em vídeos, usando rois com conexão a uma API REST.    |
| `detection-fire`              | Sistema de detecção automática de focos de incêndio em vídeo.    |

---

## 📚 Tecnologias Exploradas

- **OpenCV** – Processamento de imagem e vídeo
- **NumPy** – Manipulação numérica de arrays
- **YOLO / DeepSort (futuros)** – Detecção e rastreamento de objetos
- **Python** – Linguagem base para todos os projetos
- **Jupyter Notebooks** – Para prototipagem e visualização interativa

---

## 🧩 Estrutura do Repositório

```bash
deep-vision-hub/
├── vision-people-counting/     # Projeto de contagem de pessoas
│   ├── Sources/
│   ├── requirements.txt
│   └── README.md
│
├── smart-parking-vision/       # Sistemas de detecção de Vagas 
│   ├── models/                       
│   ├── sources/
│   ├── server/
│   ├── utils/
│   ├── config.json
│   ├── main.py
│   ├── requirements.txt
│   └── README.md  
│
├── detection-fire/             # Projeto de Detecção de incêndios
│   ├── Sources/
│   ├── config.json
│   ├── main.py
│   ├── requirements.txt
│   └── README.md      
│
├── README.md                   # Este arquivo
└── .gitignore
````

---

## 🚀 Como Utilizar

1. Clone o repositório:

```bash
git clone https://github.com/AkyLast/Deep-Vision-Hub.git
cd projeto_em_questao
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (Powershell)
venv\Scripts\Activate.ps1
```

3. Instale dependências:

```bash
pip install -r requirements.txt
```


Cada projeto contém seu próprio `README.md`,`requirements.txt` e `main.py`, permitindo instalação e execução independentes.

Exemplo:

```bash
cd vision-people-counting
pip install -r requirements.txt
python main.py
```

---

## 📌 Possíveis Expansões Futuras

* Reconhecimento facial
* OCR (leitura de texto em imagens)
* Segmentação de instâncias
* Deteção de anomalias em vídeo
* Contagem com redes neurais (YOLOv8, Detectron2, etc.)

---

## 💼 Sobre Mim

Sou interessado por resolver problemas reais com tecnologia, atuando na interseção entre **Engenharia de Software** e **Inteligência Artificial**. Meu objetivo é aplicar **IA e Visão Computacional** em projetos com impacto real — especialmente nos setores de **saúde, educação e acessibilidade**.


👨‍💻 Desenvolvido por: [Luis Fernando Ribeiro Curvelo](https://www.linkedin.com/in/luis-fernando-ribeiro-curvelo/)
Email: [luisribeiro.curvelo@gmail.com](mailto:luisribeiro.curvelo@gmail.com)

---

## 🤝 Contribuições

Sugestões, melhorias ou parcerias são bem-vindas. Sinta-se à vontade para abrir uma issue ou me chamar no LinkedIn.

---

## 📄 Licença

Este repositório é licenciado sob os termos da [MIT License](LICENSE).


