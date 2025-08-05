# 👥 Contador de Pessoas com Visão Computacional

Este projeto implementa um sistema de contagem de pessoas em tempo real utilizando técnicas de visão computacional. O sistema processa quadros de vídeo (por exemplo, filmagens de segurança ou monitoramento de escadas rolantes) para detectar movimentações em uma região definida e incrementar um contador a cada passagem detectada.

---

## 🎯 Objetivos do Projeto

- Desenvolver um sistema eficiente para contagem de pessoas **sem necessidade de sensores físicos**.
- Aplicar técnicas clássicas de processamento de imagem (thresholding adaptativo, dilatação, segmentação por região).
- Estabelecer uma base sólida para evolução do projeto com modelos de aprendizado profundo (YOLO, DeepSort, etc.).

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **OpenCV**
- **NumPy**

> Este projeto foi desenvolvido com foco em leveza e performance, sem uso de deep learning nesta fase.

---

## 📹 Como Funciona

1. O vídeo é carregado e redimensionado para padronização.
2. Uma região de interesse (ROI) é monitorada.
3. Os pixels brancos dentro dessa região são contabilizados após um processamento binário.
4. Quando a quantidade ultrapassa um determinado limite, é assumido que uma pessoa passou.
5. O contador é atualizado, e o processo se repete.

Os parâmetros são configuráveis para adaptar a diferentes contextos e ambientes.

---

## 🚀 Como Executar

```bash
# Instale as dependências
pip install -r requirements.txt

# Execute o script principal
python main.py
````

> Certifique-se de que o arquivo `escalator.mp4` (ou outro vídeo de entrada) está presente no diretório do projeto.

---

## 📈 Aplicações Reais

* Análise de fluxo em prédios inteligentes.
* Monitoramento de clientes em lojas.
* Controle de ocupação em transportes públicos.
* Verificação de cumprimento de normas de segurança (ex: capacidade máxima).

---

## 🔄 Reutilização e Expansões

Este projeto pode ser reutilizado ou expandido para diversos contextos, como:

* 🧠 Integração com **modelos de detecção de objetos** (YOLO, SSD, etc.)
* 🔁 Monitoramento com **múltiplas câmeras**
* 📱 Execução em **dispositivos embarcados** (Raspberry Pi, Jetson Nano)
* 🔍 Estimativas de densidade por **segmentação de multidões**

---

## 💡 Por Que Este Projeto é Relevante

A contagem de pessoas é uma métrica crítica para:

* Otimização de recursos (energia, segurança, pessoal)
* Melhoria da experiência do usuário (evitar superlotação)
* Conformidade com normas e regulamentações

Este projeto demonstra como é possível extrair informações úteis de vídeos usando ferramentas acessíveis e lógica bem definida.

---

## 📁 Estrutura do Projeto

```bash
vision-people-counting/
├── Sources/
│   └──  escalator.mp4             # Vídeo de entrada (não incluso no repositório)
├── main.py                        # Script principal
├── requirements.txt               # Dependências
└── README.md                      # Este arquivo
```

---

## 🤝 Contato

Fique à vontade para abrir issues ou contribuir com sugestões e melhorias.


👨‍💻 Desenvolvido por [Luis Fernando Ribeiro Curvelo](https://www.linkedin.com/in/luis-fernando-ribeiro-curvelo/)
