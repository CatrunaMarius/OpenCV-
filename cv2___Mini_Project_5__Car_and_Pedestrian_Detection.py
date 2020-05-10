import cv2
import numpy as np

#creati clasificatorul pentru oamnei
body_classifier = cv2.CascadeClassifier("D:\Programare\cv\Master OpenCV\Haarcascades\haarcascade_fullbody.xml")

#initiati capturarea video pentru fisierul video
cap = cv2.VideoCapture("D:\Programare\cv\Master OpenCV\images\walking.avi")



#bucla care incarca video cu succes
while cap.isOpened():
    #citeste primul frame
    ret, frame =cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #treceti cadrul la clasificatorul nostru 
    bodies = body_classifier.detectMultiScale(gray, 1.2,3)

    #Extrageti casute de delimitare pt orice corp identificat
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w,y+h), (0,255,255),2)
        cv2.imshow("Pedrstrians", frame)

    if cv2.waitKey(1) ==13:
        break
cap.release()
cv2.destroyAllWindows()
######################################################


import time

#creati clasificatorul pt masini
car_classifier =cv2.CascadeClassifier("D:\Programare\cv\Master OpenCV\Haarcascades\haarcascade_car.xml")

#initializea camera video dintrun fisier video
cap = cv2.VideoCapture("D:\Programare\cv\Master OpenCV\images\cars.avi")

#incarcare cu succes video
while cap.isOpened():
    time.sleep(.05)#incetineste freamul din video 
    #citeste primul frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Treceti cadrul la clasificator
    cars = car_classifier.detectMultiScale(gray, 1.4,2)

    #Extrageti casutele de delimitare pt orice corp identificat
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow("Cars", frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
