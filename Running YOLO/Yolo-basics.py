from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results = model("Images/3.jpg", save=True)
results = model("Images/2.jpg", save=True)
cv2.waitKey(0)
