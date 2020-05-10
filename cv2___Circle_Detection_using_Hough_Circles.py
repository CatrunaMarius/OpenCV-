

#cv2.HoughCircles(imagine,metoda,dp,MinDist,circle,param1,param2,minRadius,maxRadiux)
#  +metoda - disponibila in prezent doar cv2.HOUGH_GRADIENT
#  +dp -raport invers al rezolutiei acumulate
#  +MinDist - distanta minima intre centrul cercurilor detectate
#  +param1 - Valoarea gradientului utilizata in detectarea marginilor
#  +param2 - Pragul acumulatorului pentru metoda HOUGH_GRADIENT(inferior permite detectarea mai multor cercuri (fls pozitive))
#  +minRadius -limiteaza cel mai mic cerc la aceasta dimensiune( prin raza)
#  +maxRadius - stabileste in mod similar limita pt cele mai mari cercuri

import cv2
import numpy as np

image = cv2.imread("D:\Programare\cv\Master OpenCV\images\Bottlecaps.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray,5)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1.6,40,param1=100,param2=100,minRadius=25,maxRadius=60)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    #desenati cercul exterior
    cv2.circle(image,(i[0],i[1]),i[2],(255,0,0),2)

    #desenati centrul cercului
    cv2.circle(image,(i[0],i[1]),2,(0,255,0),5)

cv2.imshow("Detected Circles", image)
cv2.waitKey()
cv2.destroyAllWindows()
