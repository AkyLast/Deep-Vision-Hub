import cv2
import numpy as np

video = cv2.VideoCapture("vision-people-counting/Sources/escalator.mp4")
if not video.isOpened():
    print("❌ Erro: vídeo não foi carregado corretamente.")
    exit()

print("✅ Vídeo carregado com sucesso!")

count = 0
released = False

cv2.namedWindow("Image Gray", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Gray", 550, 360)

x, y, w, h = 490, 210, 40, 150
frame_count = 0

while True:
    ret, img = video.read()
    if not ret:
        print("⚠️ Frame não lido (fim do vídeo ou erro de leitura).")
        break
    frame_count += 1

    try:
        img = cv2.resize(img, (1100, 720))
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        imgTh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)

        kernel = np.ones((4, 4), np.uint8)
        imgDil = cv2.dilate(imgTh, kernel, iterations=2)

        cut = imgDil[y: y + h, x: x + w]
        count_whites = cv2.countNonZero(cut)

        if count_whites > 4000 and released:
            count += 1
        if count_whites < 4000:
            released = True
        else:
            released = False

        color = (0, 255, 0) if released else (250, 0, 0)                        # Green -> Liberado | Red -> Não Liberado
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness = 4)

        cv2.rectangle(imgTh, (x, y), (x + w, y + h), (250, 255, 255), thickness=6)
        cv2.putText(img, str(count_whites), (x - 30, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)  # print count whites
        cv2.rectangle(img, (575, 155), (575 + 85, 155 + 85), (250, 255, 255), thickness = -1)                   # draw background
        cv2.putText(img, str(count), (x + 100, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 4)            # print count persons

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