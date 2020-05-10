#Acestea sunt operațiuni simple care ne permit să adăugați direct sau subract  intensitatea culorii.

#Calculează funcționarea per-element a două matrice. Efectul global este în creștere sau descrescătoare a luminozității.

import cv2
import numpy as np

image = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg')

## Creați o matrice de unuri, apoi înmulțiți-l de un scalar de 100 
# Acest lucru oferă o matrice cu aceleași dimensiuni  imaginea noastră cu toate valorile fiind 100.

m =np.ones(image.shape,dtype ="uint8")*75

#Folosim acest lucru pentru a adăuga această matrice M, la imaginea noastră
# Observați creșterea luminozitatea

added = cv2.add(image, m)
cv2.imshow("Added", added)

#De asemenea, putem scădea
# Observați scăderea luminozitatea

subtracted = cv2.subtract(image,m)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey()
cv2.destroyAllWindows()


m = np.ones(image.shape, dtype="uint8")*75
print(m)