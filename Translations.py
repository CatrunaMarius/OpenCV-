import cv2
import numpy as np

image = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg')

#stoceaza inaltimea si lungimea imagini
height, width = image.shape[:2]

#extrage valorile lui Tx si Ty
quarter_height, quarter_width =height/40,width/40 # cu cat imparti la un nr cat mai mare cu atat translatarea va fi mai mica
#    | 1 0 Tx | 
#T = | 0 1 Ty |

#T este matricea noastră de translatare a imagini

T =np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])


#Folosim warpAffine pentru a transforma imaginea folosind matricea, T
img_translation = cv2.warpAffine(image, T, (width,height))
cv2.imshow('Translation', img_translation)
cv2.waitKey()
cv2.destroyAllWindows()

#Sa vedem cu arata matricea noastra T
print(T)