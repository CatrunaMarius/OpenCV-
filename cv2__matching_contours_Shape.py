

#cv2.matchShapes (șablon de contur, contur, metodă, parametru de metodă)

#Ieșire - valoare potrivire (valori inferioare înseamnă o potrivire mai strânsă)

#Șablon de contur - Acesta este conturul nostru de referință pe care încercăm să îl găsim în noua imagine
#Contur - Conturul individual pe care îl verificăm
#Metodă - Tipul de potrivire a conturului (1, 2, 3)
#Parametru metodă - lăsați singur ca 0,0 (nu este utilizat în totalitate în Python OpenCV)

import cv2
import numpy as np

#incarcam formata tablului ori imaginea de referinta
template = cv2.imread("D:\Programare\cv\Master OpenCV\images\Star.jpg", 0)
cv2.imshow('Template', template)
cv2.waitKey()

# Încărcați imaginea țintă cu formele pe care încercăm să le gasim
target = cv2.imread("D:\Programare\cv\Master OpenCV\images\shapestomatch.jpg")
target_gray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)

#Pragul ambelor imagini mai întâi înainte de a utiliza cv2.findContours
ret, thresh1 = cv2.threshold(template,127,255,0)
ret, thresh2 = cv2.threshold(target_gray,127,255,0)


#gaseste conturul in sablonului
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)#gaseste  conturul din prima imagine pe care trebuie sa il extragem


#Trebuie sa sortam contururile pe zone, astfel incat sa putem elimina cele mai mare 
#contur care este conturul imaginii
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

#Extragem al doilea cel mai mare contur, care va fi conturul sablonului nostru
template_contour = contours[1]#sunt doua conturui adica fundul alb reprezinta primulu contur si steau reprezinta al doilea contur de care am nevoi sa il extrag

#Extragem conutul din a doua imagine vizata
contours,hierarchy = cv2.findContours(thresh2,cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    #Iterate prin fiecare contur din imaginea tinta si
    #utilizam cv2.matchShapes pentru a compara formele de contur
    match = cv2.matchShapes(template_contour,c,3,0.0)#asta va da cea mai apropiata forma cautata din imaginea tinta
    print(match)
    #daca valoare lui match este sub 0,15 :
    if match <0.15:
        closest_contour =c
    else:
        closest_contour = []

cv2.drawContours(target, [closest_contour],-1, (0,255,0), 3)
cv2.imshow('Output', target)
cv2.waitKey()
cv2.destroyAllWindows()

