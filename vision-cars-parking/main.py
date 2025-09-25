import cv2
import numpy as np
import json 

class AnalyzeSpace():
    def __init__(self, frame_gray, frame_colored, start, w_h, writter_count = True):
          self.frame = frame_gray
          self.colored = frame_colored
          self.writter_count = writter_count
          self.x = start[0]
          self.y = start[1]
          self.w = w_h[0]
          self.h = w_h[1]
          self.threshold = 5000
    
    def count_white(self):
         cutted = self.frame[self.y: self.y + self.h, self.x: self.x + self.w]
         count = cv2.countNonZero(cutted)
         return count
        
    def draw_border(self):
         GREEN = (0, 255, 0)
         RED = (0, 0, 255)
         COLOR = RED if self.count_white() > self.threshold else GREEN
         cv2.rectangle(self.colored, (self.x, self.y), (self.x + self.w, self.y + self.h), color = COLOR, thickness= 6)

    def writter(self):
        self.frame = cv2.putText(self.colored, str(self.count_white()), (self.x + 10, self.y + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)  
        
    def run(self):
         self.draw_border()
         if self.writter_count:
            self.writter()
         return self.frame

with open("config.json", "r", encoding="utf-8") as file:
     data = json.load(file)

video = cv2.VideoCapture(data["video_path"])

if not video.isOpened():
    print("❌ Erro: vídeo não foi carregado corretamente.")
    exit()
print("✅ Vídeo carregado com sucesso!")

locals = data["rois"]
resize = data["resize"]
draw_countter = True if data["draw_countter"].lower() == "true" else False

cv2.namedWindow("Image Gray", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Gray", resize["grayscaled"][0], resize["grayscaled"][1])

while True:
    ret, img = video.read()
    if not ret:
        print("⚠️ img não lido (fim do vídeo ou erro de leitura).")
        break

    cv2.resize(img, resize["colored"])
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_th = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)

    kernel = np.ones(data["dilate"]["kernel"], dtype = np.uint8)
    imgDil = cv2.dilate(img_th, kernel, iterations=data["dilate"]["iterations"])
    

    for roi in locals:
        x, y, w, h, threshold = roi["x"], roi["y"], roi["w"], roi["h"], roi["threshold"]
        analyze = AnalyzeSpace(frame_gray= imgDil, frame_colored=img, start = (x, y), w_h = (w, h), writter_count=draw_countter)
        analyze.run()

    cv2.imshow("Running Parking", img)
    #cv2.imshow("Image Gray", imgDil)

    if cv2.waitKey(25) & 0xFF == ord("q"):
            print("🛑 Execução interrompida pelo usuário.")
            break

video.release()
cv2.destroyAllWindows()
print("Processamento Encerrado!")