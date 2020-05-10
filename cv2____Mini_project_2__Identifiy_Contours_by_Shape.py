
import numpy as np
import cv2

#incarca imaginea si apoi convertesteo in alb negru
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\someshapes.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("Identifying Shapes", image)
cv2.waitKey()

#Pragul imagini
ret,thresh = cv2.threshold(gray,127,255,1)

#Extragem conturul
contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    #optinem poligonul aproximativ
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)

    if len(approx)==3:# 3 reprezinta nr de puncte pe care trebuie sa lea aiba un triunghi
        shape_name = "Triangle"
        cv2.drawContours(image,[cnt],0,(0,255,0),-1)

        #gaseste centrul conturului pentru a plasa text in centru
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),1)

    elif len(approx)==4:# 4 reprezinta nr de puncte pe care trebuie sa lea aiba un patrat/dreptunghi
        x,y,w,h = cv2.boundingRect(cnt)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        #verifica pentru a vedea daca poligonul cu 4 laturi este patrat sau dreptunghi
        #cv2.boundingRect returneaza partea stanga sus si apoi inaltimea si
        if abs(w-h) <=3:#aici verificam daca lungimea si inatimea sunt egale si daca sunt atunci este un patrat daca nu sunt atungi este un dreptunghi
            shape_name = "Square"

            #goaseste centrul conturului pentru a plasa text in centru
            cv2.drawContours(image,[cnt],0,(0,125,255),-1)
            cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),1)
        else:
            shape_name = "Rectangle"
            #gaseste centrul conturului pentru a plasa text
            cv2.drawContours(image,[cnt], 0,(0,0,255), -1)
            M = cv2.moments(cnt)
            cx = int(M['m10']/M["m00"])
            cy = int(M['m01']/M["m00"])
            cv2.putText(image, shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0),1)

    elif len(approx) == 10 :#10 reprezinta nr de puncte pe care trebuie sa lea aiba pt a fi o stea
        shape_name = "Star"
        cv2.drawContours(image,[cnt],0,(255,255,0),-1)
        #gaseste centrul conturului pt a plasa text
        M= cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),1)

    elif len(approx) >=15:#>=15 reprezinca nr de puncte pe care trebuie sa le aibe pt a fi recunooscut ca un cerc
        shape_name = "Circle"
        cv2.drawContours(image,[cnt],0,(0, 255, 255),-1)

        #gaseste centrul conturului pt a plasa text
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name,(cx-50,cy), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),1)

    cv2.imshow('Identifying Shapes', image)
    cv2.waitKey()
cv2.destroyAllWindows()




