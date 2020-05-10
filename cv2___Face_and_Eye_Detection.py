#Face & Eye Detection using HAAR Cascade Classifiers
#1. Clasificatorii HAAR sunt instruiți folosind o mulțime de imagini pozitive (adică imagini cu obiectul prezent) și imagini negative (adică imagini fără obiectul prezent).

#2. Extragem apoi funcții folosind ferestre glisante din blocuri dreptunghiulare. Aceste caracteristici sunt evaluate individual și sunt calculate scăzând din negru suma intensităților de pixeli sub dreptunghiurile albe
#dreptunghiuri. Cu toate acestea, acesta este un număr ridicol de calcule, chiar și pentru o fereastră de bază de 24x24
#pixeli (180000 funcții generate). Așadar, cercetătorii au conceput o metodă numită Imagini Integrale care a calculat acest lucru cu patru referințe matrice.

#3. Cu toate acestea, mai aveau 180000 funcții, iar majoritatea nu au adăugat nicio valoare reală.

#4. Boosting a fost apoi utilizat pentru a determina cele mai informative caracteristici cu ajutorul lui Freund & Schapire AdaBoost, algoritmul ales, datorită ușurinței sale de implementare. Îmbunătățirea este procesul prin care utilizăm clasificatorii slabi pentru a construi clasificatori puternici, pur și simplu prin alocarea de penalizări mai înalte la clasificări incorecte. Reducerea caracteristicilor 180000 la 6000, ceea ce este încă destul de puțin.

#5. Gândiți-vă la asta intuitiv, dacă dintre aceste 6000 de caracteristici, unele vor fi mai informative decât altele. Ce se întâmplă dacă am folosi cele mai informative caracteristici pentru a verifica mai întâi dacă regiunea poate avea o față (falsele pozitive nu vor fi o afacere mare). Procedând astfel elimină necesitatea calculării tuturor celor 6000 de funcții simultan.

#6. Acest concept se numește cascadă de clasificatoare - pentru detectarea feței, metoda Viola Jones a folosit 38 de etape

import numpy as np
import cv2

#indicam functia CascadeClasssifier a OpenCv catre clasificator meu (format fisier) este stocat
face_classifier = cv2.CascadeClassifier("D:\Programare\cv\Master OpenCV\Haarcascades\haarcascade_frontalface_default.xml")

#incarca imaginea si convertesteo in alb negru
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\Trump.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Clasificatorul nostru returneaza ROI-ul fetei detectate ca un tuple
#Stocheaza coordonatele din stanga sus si dreapta jos 

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

#Cand nu a fost detectata nicio fata, face_classifier se intarece ca un tuple gol
if faces is ():
    print("No faces found")

#Iteram prin tabloul fetelor si desenam un dreptunghi
#peste fiecare fata din fata

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h),(127,0,255),2)
    cv2.imshow("Face Detection", image)
    cv2.waitKey()
cv2.destroyAllWindows()

################################################################











#Sa combinam detectarea fetei si a ochilor

face_classifier = cv2.CascadeClassifier("D:\Programare\cv\Master OpenCV\Haarcascades\haarcascade_frontalface_default.xml")
eye_classifier =cv2.CascadeClassifier("D:\Programare\cv\Master OpenCV\Haarcascades\haarcascade_eye.xml")

img = cv2.imread("D:\Programare\cv\Master OpenCV\images\Trump.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

#Cand nu a fost detectata nicio fata, face_classifier se intarece ca un tuple gol
if faces is ():
    print("No Face Found")

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (127,0,255),2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    #cropyn de faces
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh),(255,255,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)

cv2.destroyAllWindows()

########################################################


#haideti sa facem o detectare a fetei si a ochilor live, pastrand viziunea in permaneta
face_classifier = cv2.CascadeClassifier("D:\Programare\cv\Master OpenCV\Haarcascades\haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier("D:\Programare\cv\Master OpenCV\Haarcascades\haarcascade_eye.xml")

def face_detector(img, size=0.5):
    #conver imaginea in alb si negru
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return img

    for(x,y,w,h) in faces:
        #x = x - 50
        #w = w + 50
        #y = y + 50 
        #h = h + 50 
        cv2.rectangle(img,(x,y), (x+w, y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color=  img[y:y+h, x:x+w]
        eyes = eye_classifier.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh),(0,0,255),2)

    roi_color = cv2.flip(roi_color,1)
    return roi_color

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Faces detector", face_detector(frame))
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()

#Reglarea clasificatoarelor în cascadă
#ourClassifier.detectMultiScale (imagine de intrare, factor de scară, vecini min)

#+Factor de scară Specifica cât reducem dimensiunea imaginii de fiecare dată când facem o scară. 
#De exemplu. în detectarea feței folosim de obicei 1.3. 
#Aceasta înseamnă că reducem imaginea cu 30% de fiecare dată când este redusă.
# Valori mai mici, precum 1.05, vor dura mai mult pentru a calcula, dar vor crește rata de detectare.
#+Vecine min. Specifică numărul de vecini pe care ar trebui să-l aibă fiecare fereastră potențială pentru a-l considera o detectare pozitivă.
# De obicei setat între 3-6. Acționează ca setarea sensibilității, valorile mici vor detecta uneori mai multe fețe pe o singură față.
#  Valorile ridicate vor asigura pozitive mai puțin false, dar puteți lipsi unele fețe.