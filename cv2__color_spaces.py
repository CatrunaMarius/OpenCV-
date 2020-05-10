import cv2
import numpy as np

imagine = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg')
#let's look at the individaul color levels for the first pixel (0,0)
#BGR valorile pentru primele 0,0 pixel
B, G, R = imagine[0, 0]
print(B, G, R)
print(imagine.shape)#shape aici rezultul este in 3 dimensiuni (415,622,3)

#se vedem ce se intampla cand le convertim in alb si negru imaginea
gray_img = cv2.cvtColor(imagine,cv2.COLOR_BGR2GRAY)
print(gray_img.shape)#aici shape este in 2 dimensiuni(415,622)




#o alta spatiu de culoare util este HSV
#HSV este foarte util in filtrarea culorilor
#Hue: 0-180, Saturation:0-255, Value:0-255

imagine = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg')
hsv_imagine = cv2.cvtColor(imagine,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV imagine', hsv_imagine)#aivi va fi imaginea convertita in HSV
cv2.imshow('Hue channel', hsv_imagine[:, :, 0])#canalul Hue. : =reprezinta valorile inaltimea si lungimea pixel si 0 reprezica hue canal
cv2.imshow('Saturation channel', hsv_imagine[:, :, 1])#calnaul de saturatie. : =reprezinta valorile inaltimea si lungimea pixel si 1 reprezinta canul de saturatie
cv2.imshow('Value Channel', hsv_imagine[:, :, 2])#canalul de luminozitate/intensitate. : =reprezinta valorile inaltimea si lungimea pixel si 2 canalul de intensitate

cv2.waitKey()
cv2.destroyAllWindows()

#Haide sa ne uitam la fiecare canal in imaginea RGB#

imaginea = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg') 

#OpenCV's 'split', functia split inparte imaginea imaginea in fiecaare index de culoare
B, G, R = cv2.split(imaginea)#inparte culorile in RGB

print(B.shape)#sheap
cv2.imshow("Red", R)#imaginea in care este rosu
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

#aici vom reface imaginea la starea initiala 
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

#Aici vom amplifica culoarea albastra
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged cu amplificarea albastru", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Aici vom scoate doua din Formatu RGB si va rezulta o imagine care este formata doar din una din culorile din gama RGB

B, G, R = cv2.split(imaginea)

#aici cream o matrice de zerouri
#cu dimensiunea a imagini h x w
zero = np.zeros(imaginea.shape[:2], dtype = "uint8")

cv2.imshow("Rosu", cv2.merge([zero, zero, R]))
cv2.imshow("Verde", cv2.merge([zero, G, zero]))
cv2.imshow("Albastru", cv2.merge([B, zero, zero]))

cv2.waitKey()
cv2.destroyAllWindows()
