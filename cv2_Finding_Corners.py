import cv2
import numpy as np

#incarca imaginea si conveto in alb negru
image =cv2.imread("D:\Programare\cv\Master OpenCV\images\chess.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("original", gray)
cv2.waitKey()

#Functia cornerHarris necesita ca tipul de date al tabloului trebuie sa fie float32
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, 3, 3, 0.05)

#Folosim dilatarea punctelor de colt pentru a le mari
kernel = np.ones((7,7), np.uint8)
karris_corners = cv2.dilate(harris_corners, kernel, iterations=2)

#Pragul pt a valoare optima , poate varia in functie de imagine
image[harris_corners>0.025*harris_corners.max()] = [255, 127, 127]

cv2.imshow("Harris Corners", image)
cv2.waitKey()
cv2.destroyAllWindows()

#Harris Corner Detection este un algoritm dezvolta inca din 1998 pt detectarea colturilor
#cv2.cornerHarris(input image, block size, ksize, k)
#+input image - ar trebui să fie de nivel gri și de tip float32.
#+block size - dimensiunea cartierului considerat pentru detectarea colțului
#+ksize - parametrul de deschidere al derivatului Sobel utilizat.
#+k - parametrul fără detector de harris în ecuație
#Output - tablou de locații de colț (x, y)

#imbunatatirea Detectia de colt- good features to Track

img = cv2.imread("D:\Programare\cv\Master OpenCV\images\chess.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#precizan primele 50 de colturi
corners = cv2.goodFeaturesToTrack(gray,100,0.01,150)#poti modifica argumetele

for corner in corners:
    x,y = corner[0]
    x = int(x)
    y = int(y)
    cv2.rectangle(img,(x-10,y-10),(x+10,y+10),(0,255,0),2)

cv2.imshow("Corners Found", img)
cv2.waitKey()
cv2.destroyAllWindows()

#cv2.goodFeaturesToTrack(input image,maxCorners, qualityLevel, minDistance)
#+Input image - imagine pe un singur canal cu 8 biti sau floating-point 32 de biti
#+maxCorners - Numarul maxim de colturi de intoarcere. daca exista mai multe colturi decat se gasesc, cele mai puternic dintre ele este returnat.
#+qualityLevel - Parametru care caracterizeaza calitatea minima acceptata a colturilor de imagine.
#   Valoarea parametrului este inmultita cu cea mai buna masura a calitati coltului(valoarea cea mai mica a valorii proprii).
#   Colturile cu masura de calitatea mai mica decat produsul sunt respinse.
#   de exemplu daca cel mai bun colt are masura de calitate = 1500, iar qualityLevel = 0.01,
#   atunci toate colturile cu calitatea -- masura mai mica de 15 sunt respinse.
#+minDistance - Distanta minima euclidiana posibila intre colturile intoarse

#algoritmul de detectare colturi are problem atunci cand imaginea are o intensitate a lumini ridicata sau atunci cand imaginea scalata