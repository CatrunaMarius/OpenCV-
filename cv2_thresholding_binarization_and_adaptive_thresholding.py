#În acest moment, convertim o imagine la scară gri la forma sa binară
#cv2.threshold(image, Threshold Value, Max Value, Threshold Type)
#Threshold Type:
#cv2.THRESH_BINARY -cel mai comun
#cv2.THRESH_BINARY_INV -cel mai comun
#cv2.THRESH_TRUNC
#cv2.THRESH_TOZERO
#cv2.THRESH_TOZERO_INV
import cv2
import numpy as np



#incarcam imaginea ca alb negru(gri)
image = cv2.imread('D:\Programare\cv\Master OpenCV\images\gradient.jpg',0)
cv2.imshow('Original',image)

#Valorile care sunt sub 127 merg la 0(negru),toate care sunt peste merg la 255(alb)
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow("1 Threshold Binary", thresh1)

#Valoaril sub 127 pleaca catre 255 si valorile care sunt peste 127 merga la 0
ret,thresh2 = cv2.threshold(image,227,255,cv2.THRESH_BINARY_INV)
cv2.imshow("2 Threshold Bonary Inverse", thresh2)

#Valorile care sunt peste 127 sunt tuncheate (reținute) la 127 (argumentul 255 este neutilizat)
ret,thrash3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('3 Thresh Thunc', thrash3)

#Valorile sub 127 sunt la 0, peste 127 sunt neschimbate
ret,thrash4 = cv2.threshold(image,127,255, cv2.THRESH_TOZERO)
cv2.imshow('4 Thresh Tozero', thrash4)

# Resetarea de mai sus, sub 127 este neschimbată, peste 127 merge la 0
ret,thrash5 = cv2.threshold(image, 127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("5 THRESH TOZERO INV", thrash5)
cv2.waitKey()
cv2.destroyAllWindows()

#Există un mod mai bun de a evita pragul?
#Cea mai mare cădere a acestor metode simple de prag este că trebuie să furnizăm valoarea pragului (adică valoarea 127 pe care am folosit-o anterior).

#Ce se întâmplă dacă ar exista un mod mai inteligent de a face acest lucru?
#Există un prag adaptativ.

#cv2.adaptiveThreshold(image, Max Value , Adaptive Type,Threshold Type, block size, constantă care este scăzută din medie)
#Adaptive Type:
#cv2.ADAPTIVE_THRESH_MEAN_C -bazat pe media pixeli din apropiere
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C -suma ponderată a pixelilor din apropiere de sub fereastra gaussiană
#cv2.THRESH_OTSU(folosește funcția cv2.threshold) - algoritmul cyclever presupune că există două picuri în histograma la scară gri a imaginii și apoi încearcă să găsească o valoare optimă pentru a separa aceste două vârfuri pentru a găsi T.
#Incarcam o noua imaginea
image = cv2.imread('D:\Programare\cv\Master OpenCV\images\Origin_of_Species.jpg', 0)

cv2.imshow('Oringinal', image)
cv2.waitKey()

#Valorile care sunt sub 127 merg la 0(negru),toate care sunt peste merg la 255(alb)
ret,thresh1 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh1)
cv2.waitKey()

#Este o practică bună pentru a blur imaginile, deoarece elimină zgomotul
image = cv2.GaussianBlur(image,(3,3),0)

#Folosim adaptiveThreshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 3, 5)
cv2.imshow("Adaptive Mean Threshoding", thresh)
cv2.waitKey()

_, th2 =cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Guassian Otsu's Thresholding", th2)
cv2.waitKey()

#Pragul lui Otsu după filtrarea gaussiană
blur = cv2.GaussianBlur(image,(5,5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Guassian Otsu's Thresholding", th3)
cv2.waitKey()
cv2.destroyAllWindows()
