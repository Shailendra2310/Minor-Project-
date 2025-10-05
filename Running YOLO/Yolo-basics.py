from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results = model("Images/friends.jpg", save=True)
cv2.waitKey(0)
