import cv2
import numpy as np
from utils.save_logs import registrar_log
from utils.connection import update_parking

class StatusRois():
    def __init__(self, id_roi: int, parking, status_server: bool = False):
          self.id_roi = id_roi
          self.parking = parking
          self.limiter = 5
          self.status = False
          self.status_server = status_server

    def analyze_roi(self, new_status = False):
        status_update = self.status
        if self.status != new_status:
             self.limiter -= 1
             if self.limiter == 0:
                  self.limiter = 5
                  status_update = new_status 
                  self.status = status_update
                  if self.status_server:
                    update_parking(parking=self.parking, vaga_id=self.id_roi, status=status_update)
                  else:
                    self.save_log()
        else:
             self.limiter = 5
        return status_update
    
    def save_log(self):
         try: 
              registrar_log(id_vaga=self.id_roi, parking=self.parking, status=self.status)
         except Exception as e:
              print("Erro ao salvar o log:", e)

class AnalyzeSpace():
     def __init__(
             self, frame_gray, frame_colored, id_roi, start, w_h, writter_count = True, roi_statusClass = None, threshold = 5000, parking: str = "condPark", statusDraw_idVaga = False
             ):
          self.frame = frame_gray
          self.colored = frame_colored
          self.id_roi = id_roi
          self.x = start[0]
          self.y = start[1]
          self.w = w_h[0]
          self.h = w_h[1]

          self.writter_count = writter_count
          self.statusDraw_idVaga = statusDraw_idVaga

          self.parking = parking
          self.roi_statusClass = roi_statusClass
          self.released = 0
          self.threshold = threshold
    
     def count_white(self):
         cutted = self.frame[self.y: self.y + self.h, self.x: self.x + self.w]
         count = cv2.countNonZero(cutted)
         return count
        
     def draw_border(self):
         GREEN = (0, 255, 0)
         RED = (0, 0, 255)
         status = self.count_white() > self.threshold
         self.roi_statusClass.analyze_roi(status)
         if status:
              COLOR = RED
              self.released += 1
         else: 
              COLOR = GREEN
         cv2.rectangle(self.colored, (self.x, self.y), (self.x + self.w, self.y + self.h), color = COLOR, thickness= 4)

     def writter(self):
        x = self.x + 10 if self.parking == "condPark" else self.x
        self.frame = cv2.putText(self.colored, str(self.count_white()), (x, self.y + 8), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3) 

     def draw_placar(self):
        COLOR = (255, 0, 0)
        if self.parking == "condPark":
          X_i = (self.x + (self.x + self.w)) // 2
          prop = self.w // 3
          pointText_X = X_i - 10 if self.id_roi < 10 else X_i - 20
          cv2.rectangle(self.colored, (X_i - prop, self.y - 45), (X_i + prop, self.y - 15), color = COLOR, thickness= -1)
          cv2.putText(self.colored, str(self.id_roi), (pointText_X, self.y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) 
        else: 
          loc_x = (self.x + self.w - 30, self.x + self.w + 2)
          x_i = -1 if self.id_roi < 10 else 4
          prop_x = (self.x + self.w - (self.x + self.w - 30)) // 3 - x_i
          prop = self.h // 3
          cv2.rectangle(self.colored, (loc_x[0], self.y - 2), (loc_x[1], self.y + 20), color = COLOR, thickness= -1)
          cv2.putText(self.colored, str(self.id_roi), ((loc_x[0]) + prop_x, self.y + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2) 

     def run(self):
         self.draw_border()
         if self.writter_count:
            self.writter()
         if self.statusDraw_idVaga:
            self.draw_placar()
         return self.frame
