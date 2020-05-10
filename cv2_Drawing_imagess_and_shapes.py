import cv2
import numpy as np

#creare o imagine neagra
imagine = np.zeros((512,512,3),np.uint8)

#putem face aceasta in black si alb?
imaginea_bw = np.zeros((515,515), np.uint8)

cv2.imshow("black Rectangle(Color)", imagine)
cv2.imshow("black Rectangle(B&W)", imaginea_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()



#Să trasăm o linie peste pătratul nostru negru 
#cv2.line(imaginea, starting cordinates, ending cordinates, color, thickness)# thickess reprezinta nr de pixel folositi pt a trasa o line
imaginea = np.zeros((512,512,3), np.uint8)
cv2.line(imaginea, (0,0), (512,512), (255,127,0), 5)
cv2.imshow("Blue Line", imaginea)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Să desenăm acum un dreptunghi
#cv2.rectangle(image, starting vertex, opposite vertex, color(RGB), thickness)

imaginea = np.zeros((512,512,3), np.uint8)

cv2.rectangle(imaginea, (100,100), (300,250), (127,50,127), -1) #daca thickness este -1 atuci dreptunghiul se va umple
cv2.imshow("Rectangle", imaginea)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ce spuneti de cercuri?
#cv2.cirlce(image, center, radius, color, fill)
imaginea = np.zeros((512,512,3), np.uint8)
cv2.circle(imaginea,(350,350), 100, (15,75,50), -1)
cv2.imshow("Circle", imaginea)
cv2.waitKey(0)
cv2.destroyAllWindows()

#si polygons?
imaginea = np.zeros((512,512,3), np.uint8)

#definim patru puncte
pts = np.array([[10,50],[400,50],[90,200],[50,500]],np.int32)

#acum reshape puntele noastre in formatul care ne trebuie pt polylines
pts = pts.reshape((-1,1,2))

cv2.polylines(imaginea,[pts], True, (0,0,255),3)
cv2.imshow("Polygon", imaginea)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Hai să adăugăm chiar text cu cv2.putText
#cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)

    #acestea sunt fomratele de scriere
    #FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN
    #FONT_HERSHEY_DUPLEX,FONT_HERSHEY_COMPLEX
    #FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
    #FONT_HERSHEY_SCRIPT_SIMPLEX
    #FONT_HERSHEY_SCRIPT_COMPLEX

imagine  = np.zeros((512,512,3),np.uint8)

cv2.putText(imagine, "Mars", (75,290), cv2.FONT_HERSHEY_COMPLEX, 2,(100,170,0), 3)
cv2.imshow("Mars", imagine)
cv2.waitKey(0)
cv2.destroyAllWindows()

