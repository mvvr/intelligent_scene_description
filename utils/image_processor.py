import cv2
import numpy as np
from yolov5 import YOLO

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
    # Example: YOLO object detection
    yolo = YOLO("yolov5s")
    results = yolo.detect(frame)
    return results
