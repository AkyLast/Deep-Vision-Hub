import os, cv2, numpy as np, json
from models.roi_analyzer import StatusRois, AnalyzeSpace
from utils.connection import connect, set_parking

with open("config.json", "r", encoding="utf-8") as file:
     data = json.load(file)

# Video Configuration 
VIDEOS_CONFIG = data["videos_config"]
VIDEOS_PATH = VIDEOS_CONFIG["video_colored"]["video_path"][0]
PARK_NAME = os.path.splitext(os.path.basename(VIDEOS_PATH))[0] if not isinstance(VIDEOS_PATH, int) else "None"

# Rois Configurations
try:
    ROIS = data["rois"][PARK_NAME]
    DILATE = data["dilate"][PARK_NAME]
except Exception as e:
    print("Caminho do video não identificado")
    ROIS = []
    DILATE = {"kernel": [2,2], "iterations": 1}
status_drawCounter = VIDEOS_CONFIG["video_colored"]["statusDraw_Counter"]
statusDraw_idVaga = VIDEOS_CONFIG["video_colored"]["statusDraw_idVaga"]

# Counting Area Configuration
AREA_CONFIG = data["counting_area_config"]
LOCAL = AREA_CONFIG["local"]["bottom-right"]


def run():
    STATUS_SERVER = data["status_server"]
    if STATUS_SERVER == 1:
        try:
            connect()
            print("Rodando com o servidor!")
        except Exception as e:
            print("Erro ao conectar com o servidor:", e)
            print("Rodando internamente.")
            STATUS_SERVER = 0

    Rois_Class = {f"roi_{roi["id_roi"]}": StatusRois(roi["id_roi"], parking = PARK_NAME, ) for _, roi in enumerate(ROIS)}
    if STATUS_SERVER: set_parking(data=ROIS, name=PARK_NAME)

    video = cv2.VideoCapture(VIDEOS_PATH)
    if not video.isOpened():
        print("❌ Erro: vídeo não foi carregado corretamente.")
        exit()
    print("✅ Vídeo carregado com sucesso!")
    
    if VIDEOS_CONFIG["video_grayscaled"]["status"]:
        cv2.namedWindow("Image Gray", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Image Gray", VIDEOS_CONFIG["video_grayscaled"]["size"][0], VIDEOS_CONFIG["video_grayscaled"]["size"][1])

    while True:
        ret, img = video.read()
        if not ret:
            print("⚠️ img não lido (fim do vídeo ou erro de leitura).")
            break
        
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gaussian_gray = cv2.GaussianBlur(img_gray, (9, 9), 1)

        img_th = cv2.adaptiveThreshold(gaussian_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 12)
        kernel = np.ones(DILATE["kernel"], dtype = np.uint8)
        imgDil = cv2.dilate(img_th, kernel, iterations=DILATE["iterations"])
        
        realeased = len(ROIS)
        for roi, roi_statusClass in zip(ROIS, Rois_Class.values()):
            id, x, y, w, h, threshold = roi["id_roi"], roi["x"], roi["y"], roi["w"], roi["h"], roi["threshold"]
            analyze = AnalyzeSpace(
                frame_gray= imgDil, frame_colored=img, id_roi=id, start = (x, y), w_h = (w, h), 
                roi_statusClass=roi_statusClass, threshold=threshold, parking=PARK_NAME, 
                writter_count=status_drawCounter, statusDraw_idVaga=statusDraw_idVaga
                )
            analyze.run()
            realeased -= analyze.released

        img = cv2.resize(img, VIDEOS_CONFIG["video_colored"]["size"])

        # Counting Area
        LOCAL_TEXT = LOCAL["textStart-M"] if realeased<10 else LOCAL["textStart"]
        cv2.rectangle(img, LOCAL["start"], LOCAL["end"], AREA_CONFIG["color"], thickness=-1)
        cv2.putText(img, f"{str(realeased)}/{len(ROIS)}", LOCAL_TEXT, cv2.FONT_HERSHEY_SIMPLEX, 1, AREA_CONFIG["colorText"], 4)  
        
        # Images Shows
        cv2.imshow("Running Parking", img)
        if VIDEOS_CONFIG["video_grayscaled"]["status"]:
             cv2.imshow("Image Gray", imgDil)

        if cv2.waitKey(25) & 0xFF == ord("q"):
             print("🛑 Execução interrompida pelo usuário.")
             break

    video.release()
    cv2.destroyAllWindows()
    print("Processamento Encerrado!")

if __name__ == "__main__":
    run()