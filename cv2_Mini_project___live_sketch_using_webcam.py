import cv2
import numpy as np

#Funcția noastră generatoare de schițe
def sketch(image):
    # convert imaginea catre alb negru
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 

    # Curățați imaginea folosind blur gaussian
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5), 0)

    # Extrage marginile
    canny_edges = cv2.Canny(img_gray_blur, 20, 50)# poti modifica ultimi doi parametri pt a avea mai multe sau mai putine lini

    # Efectuați o inversare binarizând a imagini
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

#initializeaza camera web, cap este obiectul furnizat de videocapture
#Contine un boolean care indica daca a avut succes (ret)
#Contine de asemenea, imaginile colectate de webcam(cadrul)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Live Sckita", sketch(frame))
    if cv2.waitKey(1)==13: #13 este chia enter
        break

#Eliberati camera si inchideti fereastrele
cap.release()
cv2.destroyAllWindows()

