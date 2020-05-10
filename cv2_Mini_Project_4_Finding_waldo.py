import cv2
import numpy as np

#incarcare imagine si convertire in alb negru
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\WaldoBeach.jpg")
cv2.imshow("Where is Waldo?", image)
cv2.waitKey()
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#incarca shablonul imagini
template = cv2.imread("D:\Programare\cv\Master OpenCV\images\waldo.jpg",0)

result = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF)#gaseste sablonul care se potriveste. cv2.TM_CCOEFF este una din metode pt a gasi potrivirea
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)#da coordonatel in care a fost gasita potrivirea

#Creați caseta de legare
#astea foloseste punctele gasite pt a crea un  dreptunghi
top_left = max_loc
bottom_right = (top_left[0] +50,top_left[1]+50)#+50 pt a ingrosa dreptunghiul
cv2.rectangle(image, top_left,bottom_right,(0,0,255),5)#astea sunt folosite pt a creea un dreptunghi rosu cand a fost gasit potrivirea

cv2.imshow("Where is Waldo?", image)
cv2.waitKey()
cv2.destroyAllWindows()

#note privind potrivirea sablonului
#Exista o varietate de metode pentru a efectua potrivirea sabloanelor,
#dar in acest caz folosim coeficientul de corelatie specificat de indicatorul cv2.TM_CCOEFF.

#Deci, ce face exact functia cv2.matchTemplate?
#In esenta, aceasta functie ia o "fereastra glisanta" a imagini noastre de interogare waldo 
#si o gliseaza pe imaginea noastra de pazzle de la stanga la dreaptasi de sus in jos,cate un pixa.
#Apoi pentru fiecare dintre aceste locatii calculam coeficientul de corelatie pt a determina cat de "bun" sau "rau" este.

#Regiunea cu o corelatie suficient de ridicata pot fi considerate "potriviri" pt modelul nostru waldo.
#De acolo nu ne ramane decat sa apelam la cv2.minMaxLoc pt a afla unde sunt potrivirile noastre "bune"
#Cu adevarat, nu este decat sa se potriveasca sabloanel

#metode folosite pentru as gasi potrivirile:
#cv2.TM_CCOEFF
#cv2.TM_CCOEFF_NORMED
#cv2.TM_CCORR         -gresit pt exemplul nostru
#cv2.TM_CCORR_NORMED
#cv2.TM_SQDIFF        -gresit pt exemplul nostru
#cv2.TM_SQDIFF_NORMED -gresit pt exemplul nostru
