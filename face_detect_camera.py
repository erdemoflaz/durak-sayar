#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import cv2
import imageio

face_cascade = cv2.CascadeClassifier('data/haarcascade-frontalface-default.xml')

empty_chair = 1.0
bus_chair_limit = 1.0

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, ((0,frame.shape[0] -100)),(360, frame.shape[0]), (255,255,255), -1)
        cv2.putText(frame, "Duraktaki bekleyen insan: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        cv2.putText(frame, "Otobus koltuk sayisi: " + str(int(bus_chair_limit)), (0,frame.shape[0] -30), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        cv2.putText(frame, "Gelen otobusteki bos koltuk sayisi: " + str(int(empty_chair)), (0,frame.shape[0] -50), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

        waiting_people = faces.shape[0]

        if waiting_people > empty_chair:
            bus_count = math.ceil((waiting_people - empty_chair) / bus_chair_limit)
            cv2.putText(frame, "Kalkacak otobus: " + str(int(bus_count)), (0,frame.shape[0] -70), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    canvas = detect(frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
