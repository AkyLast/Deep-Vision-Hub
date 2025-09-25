import cv2
import json
import numpy as np

with open("config.json", "r") as file:
    data = json.load(file)

VIDEO_CONFIG = data["video_config"]
DILLATE_CONFIG = data["dillate"]
THRESHOLD_ROI = data["threshold_roi"]
AREA_COUNT = data["area_count"]
x, y, w, h = data["xywh"]

video = cv2.VideoCapture(VIDEO_CONFIG["video_path"])
if not video.isOpened():
    print("❌ Erro: vídeo não foi carregado corretamente.")
    exit()

print("✅ Vídeo carregado com sucesso!")

count = 0
released = False
frame_count = 0

cv2.namedWindow("Image Gray", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Gray", 550, 360)

while True:
    ret, img = video.read()
    if not ret:
        print("⚠️ Frame não lido (fim do vídeo ou erro de leitura).")
        break
    frame_count += 1

    try:
        img = cv2.resize(img, VIDEO_CONFIG["video_size"])
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        imgTh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)

        kernel = np.ones(DILLATE_CONFIG["kernel"], np.uint8)
        imgDil = cv2.dilate(imgTh, kernel, iterations=DILLATE_CONFIG["iterations"])

        cut = imgDil[y: y + h, x: x + w]
        count_whites = cv2.countNonZero(cut)

        if count_whites > THRESHOLD_ROI["gateway"] and released:
            count += 1
            released = False  
        elif count_whites < THRESHOLD_ROI["escape"]:
            released = True

        color = (0, 255, 0) if released else (250, 0, 0)                      
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness = 4)

        cv2.rectangle(imgTh, (x, y), (x + w, y + h), (250, 255, 255), thickness=6)
        #cv2.putText(img, str(count_whites), (x - 30, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1) 
        if AREA_COUNT["status"].lower() == "true":
            cv2.rectangle(img, AREA_COUNT["start"], AREA_COUNT["end"], AREA_COUNT["color"], thickness = -1)                 
            cv2.putText(img, str(count), AREA_COUNT["startText"], cv2.FONT_HERSHEY_SIMPLEX, 3, AREA_COUNT["textColor"], 4)        

        cv2.imshow("Video running", img)
        cv2.imshow("Image Gray", imgTh)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            print("🛑 Execução interrompida pelo usuário.")
            break

    except Exception as e:
        print(f"❌ Erro no frame {frame_count}: {e}")
        break

video.release()
cv2.destroyAllWindows()
print("Processamento finalizado.")