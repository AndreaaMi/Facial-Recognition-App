from ultralytics import YOLO
import cv2
model = YOLO('../Yolo-Weights/yolov8n.pt') #weights
results = model("Images/1.png", show = True) #path, show - nshowing confident level
cv2.waitKey(0) #unless the user inputs don't do anything
#iage with detection values
