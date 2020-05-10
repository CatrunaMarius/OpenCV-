#Detectarea liniei - folosind linile Hough
#cv2.HoughLines(imagine binarizata/pragul, p precizie, 0 precizie, prag)
#pragul este votul minim pentru ca acesta sa fie considerat o linie
#p =este distanta perpendiculara de la origine
#0 =este unghiul format de nomalul acestei linii fata de origine(masurat in radieni)
import cv2
import numpy as np

image = cv2.imread("D:\Programare\cv\Master OpenCV\images\soduku.jpg")

#conversia RGB2GRAY si extregerea margnilor Canny
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,170,apertureSize =3)

cv2.imshow("edges",edges)
cv2.waitKey()

#rulati HounghLines folosind o precizie rho de 1 pixel
#exactitatea np.pi/180 care este de 1 grad
#pragul de linie este setat la 240 (nr de puncte pe linie)

lines = cv2.HoughLines(edges,1,np.pi/180,250) #genereaza linii 

#Vom itera fiecare linie si o convertim intr-un format
#solicitat de cv2.lines(adica necesita puncte finale)
#linile au rho si theta valori
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image,(x1,y1), (x2,y2),(255,0,0),2)
cv2.imshow("Hough Lines", image)
cv2.waitKey()
cv2.destroyAllWindows()

#Probabilitatea lini Hough
#cv2.HoughLinesP(imagine binarizata,p precizie, 0 precizie, prag,lungime minima a liniei, decalaj maxim de linie)

image =cv2.imread("D:\Programare\cv\Master OpenCV\images\soduku.jpg")

#conversia RGB2GRAY si extregerea margnilor Canny
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,170,apertureSize = 3)

#din nou folosim acelasi prezizie Rho si Theta
#Cu toate acestea, specificam un vot minim (pts de-a lungul liniei) de 100
#si lungimea minima a liniei de 5 pixeli si distanta maxima intre liniile de 10 pixeli

lines = cv2.HoughLinesP(edges,1,np.pi/180,200,5,10)
print(lines.shape)

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
cv2.imshow("Probabilistic Hough Lines", image)
cv2.waitKey()
cv2.destroyAllWindows()