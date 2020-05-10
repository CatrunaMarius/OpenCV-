import cv2
import numpy as np

#incarcam o imagine simpla cu 3 patrate negre
#image = cv2.imread('D:\Programare\cv\Master OpenCV\images\shapes_donut.jpg')
image = cv2.imread('D:\Programare\cv\Master OpenCV\images\shapes.jpg')
cv2.imshow("Input Image", image)
cv2.waitKey()

#alb negru
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#gaseste marginile canny
#aceasta nu este necesare dar este utila pt a indeparta noise
edged = cv2.Canny(image,30,200)
cv2.imshow('Canndy Edges', edged)
cv2.waitKey()

#gaseste contururile
#Utilicati o copie a imagini de ex. edged.copy(), deoarece findContours modifica imaginea
#Contours sunt linii continue sau curbe care au legat sau acoperă limita completă a unui obiect dintr-o imagine
#Contours sunt foarte importante în: Detectarea obiectelor și Analiza formei
#OpenCV stocheaza Contours intro lista a listelor
#hierarchy in contours
#hierarchy types (primele două sunt cele mai utile)
#cv2.RETR_LIST -prea toate contours
#cv2.RETR_EXTERNAL-prea doar contururile externe sau exterioare
#cv2.RETR_CCOMP -prea totul într-un heirarchy cu 2 niveluri
#cv2.RETR_TREE -prea toate în ierarhie completă

#contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours,hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Counturing', edged)
cv2.waitKey(0)


print("Number of Contours found = " +str(len(contours)))

#cv2.drawContours(image,contours, punctele conturs, culoarea RGB,)
cv2.drawContours(image,contours, -1, (0,255,0), 3)

cv2.imshow('Conturs', image)
cv2.waitKey()
cv2.destroyAllWindows()

#cv2.findContours (imagine, Mod de recuperare, Metodă de aproximare)

#Returnări -> ret, contururi, ierarhie

#NOTĂ
#În OpenCV 2.X, findContours returnează doar 2 argumente care sunt contururi, ierarhie

#Dacă utilizați OpenCV 2.X înlocuiți linia 12 cu:

#contururi, ierarhie = cv2.findContours (imagine, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#Variabila „contururi” este stocată ca un tablou numpy de puncte (x, y) care formează conturul

#În timp ce „ierarhie” descrie relațiile copil-părinte între contururi (adică contururile din contururi)

#Metode de aproximare
#Folosind cv2.CHAIN_APPROX_NONE stochează toate punctele de delimitare. Dar nu avem nevoie neapărat de toate punctele de delimitare. Dacă punctele formează o linie dreaptă, nu avem nevoie decât de punctele de început și de încheiere ale acestei linii.

#acesta de jos este mult mai eficienta
#Utilizarea cv2.CHAIN_APPROX_SIMPLE oferă în schimb aceste puncte de început și de sfârșit ale contururilor de delimitare, ceea ce duce la o stocare mult mai eficientă a informațiilor de contur ..


