import cv2
import json
import cvzone

from ultralytics import YOLO

with open("config.json", "r") as file:
     data = json.load(file)

VIDEOS = data["videos_path"]
VIDEO_SIZE = data["video_size"]

video = cv2.VideoCapture(VIDEOS[0])
model = YOLO(data["model_path"])

while True:
    ret, frame = video.read()
    if not ret:
        print("⚠️frame não lido, fim do vídeo ou erro de leitura.")
        break

    frame = cv2.resize(frame, VIDEO_SIZE)

    resul = model.predict(frame, conf = 0.5, verbose = False)
    for obj in resul[0].boxes:
        x1, y1, x2, y2 = [int(i) for i in obj.xyxy[0]]
        cv2.rectangle(frame, (x1, y1), (x2, y2), color = (255, 0, 0), thickness = 2)

        area = (x2-x1) * (y2-y1)
        prop = area/(VIDEO_SIZE[0] * VIDEO_SIZE[1])
        cvzone.putTextRect(frame, f"{prop*100:.2f}%", (x1, y1 + 10), scale = 1.2, thickness=2, colorR=(255, 0, 0))
        if prop>=data["proporcao_min"]:
            cvzone.putTextRect(frame,"Alerta! Fogo Descontrolado",(50,50),colorR=(0,0,255))
            cv2.rectangle(frame, (x1, y1), (x2, y2), color = (0, 0, 255), thickness = 2)
            cvzone.putTextRect(frame, f"{prop*100:.2f}%", (x1, y1 + 10), scale = 1.2, thickness=2, colorR=(0, 0, 255))

    cv2.imshow("Monitoring", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
            print("🛑 Execução interrompida pelo usuário.")
            break

video.release()
cv2.destroyAllWindows()
print("Processamento Encerrado!")