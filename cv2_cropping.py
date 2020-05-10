import cv2
import numpy as np

image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")
height, width = image.shape[:2]

#asta se spune de unde incepe cordonatele pixalurilor(crem un dreptunghi pentru  cropping)
start_row, start_col = int(height*.25), int(width*.25) #pt a crea un dreptunghi aici am aproximat cam cat la sunt(.25 adica 25%) din imagine este inceputul dreptunghiului

#asta spune unde se termina coordonatele pixelurilor
end_row, end_col = int(height*.75), int(width*.75)#aici am aproximat cam cat la sunt(.75 adica 75%) din imagine este sfarsitul dreptunghiului

#Pur și simplu utilizați indexare pentru a decupla dreptunghiul dorim
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow("Original Image", image)
cv2.waitKey()
cv2.imshow("Cropped Image", cropped)
cv2.waitKey()
cv2.destroyAllWindows()