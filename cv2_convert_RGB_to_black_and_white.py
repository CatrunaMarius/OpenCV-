import cv2

#incarca imaginea de intrare
imagine = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")#cv2imread va citi imaginea din fisierul ales, iar in interorul parantezei este calea catre imaginea aleasa
cv2.imshow('Original', imagine)#cv.imshow va arata imaginea aleasa de noi, "original" reprezinta titlul imagini si al doilea argument repreziva variabila pe care am setato mai sus
cv2.waitKey()

#cream o variabila care transforma imagnea noastra color in alb si negru
gray_imagine = cv2.cvtColor(imagine,cv2.COLOR_BGR2GRAY)

#aici vom arata poza transformata in alb negru
cv2.imshow('grayscale',gray_imagine)
cv2.waitKey()
cv2.destroyAllWindows()#aceasta este importata atuci cand inchidem fereastra petru a nu distruge programul


#metoda mai rapida
img =cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg',0)# aici zero se refera la faptul ca va transforma imaginea colora in alb si negru

cv2.imshow('grayscale', img)
cv2.waitKey()
cv2.destroyAllWindows()