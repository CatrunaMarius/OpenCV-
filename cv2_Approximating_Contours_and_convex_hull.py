
#cv2.approxPolyDP(contour, Approximation Accuracy, Closed)
#contour - este conturul individual pe care dorim sa-l aproximam
#Acuratarea aproximarii - Parametrul important este determinarea exactitatii aproximarii.
# valorile mici dau aproximari precise, valorile mari ofera o aproximare mai generica. 
# O regula buna este mai mica de 5% din perimetrul conturului
#Closed - o valoare booleana care precizeaza daca conturul aproximativ ar trebui sa fie deschis sau inchis

import numpy as np
import cv2 

#incarca imaginea si pastreaza o copie
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\house.jpg")
orig_image = image.copy()
cv2.imshow('Original Image', orig_image)
cv2.waitKey()

#convert imaginea in alb negru si biarizare
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

##gaseste contururile
contours, hierachy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

## Iterate prin fiecare contur și calculează dreptunghiul de delimitare
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(orig_image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('Bounding Rectangle', orig_image)
cv2.waitKey()

#iteram pri fiecare contur si calculeaza conturul aproximativ
for c in contours:
    # Calculați precizia ca procent din perimetrul conturului
    accuracy = 0.03 *cv2.arcLength(c,True)#aici te poti juca cu procentrul de acurate(0.03) in unle situati poat diferi
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0,(0,255,0),2)
    cv2.imshow("Approx Poly DP", image)

cv2.waitKey()
cv2.destroyAllWindows()


#Convex Hull

image = cv2.imread("D:\Programare\cv\Master OpenCV\images\hand.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image', image)
cv2.waitKey()

#prag de imagine/Threshold the image
ret, thresh = cv2.threshold(gray,176,255,0)

#gaseste conturul 
#(hierarchy=ierarhie)
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#Sortati contururile pe zone si apoi eliminati cel mai mare conut cadru
n = len(contours)-1 #fara acel -1 va aparea o alta cutie deoarece este pe fond alb
contours = sorted(contours, key= cv2.contourArea, reverse=False)[:n]

#Iterate through contours and draw the convex hull
for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image, [hull], 0, (0,255,0),2)
    cv2.imshow("Convex Hull", image)

cv2.waitKey()
cv2.destroyAllWindows()

