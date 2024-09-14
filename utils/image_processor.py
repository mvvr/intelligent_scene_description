import torch
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.general import non_max_suppression
import cv2

def extract_frames(video):
    cap = cv2.VideoCapture(video)
    frames = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()
    return frames

def detect_objects(frame):
    model = DetectMultiBackend(weights='yolov5s.pt')  # Load YOLOv5 model
    img = [frame]  # Convert frame to a list (YOLOv5 expects a batch of images)
    results = model(img)
    detections = non_max_suppression(results)[0]
    return detections
