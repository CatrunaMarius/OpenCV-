import cv2
import numpy as np

#Sunt trei mari tipuri de dectectare margini uni obiect din imagine:
# -Sobel -pentru a evidenția marginile verticale sau orizontale
# -Laplacian - ia toate marginile orizontal
# -Canny -Optim datorită ratei de eroare scăzute, marginilor bine definite și detectării precise

#Canny edge Dectectin Algoritm
#  1. Aplica Gaussian Blurring
#  2.gaseste intensitatea gradient al imaginii
#  3. Aplica non-maxim supresie(adica elimina pixeli care nu sunt margini)
#  4.Hysteresis(Isteraza) - Aplica thresholds(adica daca pixelul se afla in pragurile superioare si inferioare, este considerat o margine


image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg",0)

#height, width = image.shape

#Estrage marginle Sobel
sobel_x = cv2.Sobel(image, cv2.CV_8U, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=5)


cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.imshow('Sobel X', sobel_x)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel_OR', sobel_OR)
cv2.waitKey()

lapacian = cv2.Laplacian(image,cv2.CV_8U)
cv2.imshow('Laplacian', lapacian)
cv2.waitKey()

## Apoi, trebuie să oferim două valori: prag1 și prag2. Orice valoare a gradientului mai mare decât pragul2
# este considerat a fi o margine. Orice valoare sub pragul1 este considerată a nu fi o margine.
# Valorile cuprinse între pragul 1 și pragul2 sunt clasificate ca muchii sau non-margini în funcție de modul lor
#intensitățile sunt „conectate”. În acest caz, orice valori de gradient sub 60 sunt considerate non-muchii
#unde oricare valori peste 120 sunt considerate muchii.

#Canny Edge Detection utilizează valorile gradientului ca praguri
# Primul prag gradient
canny = cv2.Canny(image, 50, 120)
cv2.imshow("Canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()