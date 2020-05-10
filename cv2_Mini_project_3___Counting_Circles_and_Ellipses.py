
import cv2
import numpy as np

#incarca imaginea
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\Blobs.jpg",0)
cv2.imshow('Original Image',image)
cv2.waitKey()

#initializti detectorul folosind parametrii impliciti
detector = cv2.SimpleBlobDetector_create()

#Detect blobs
keypoints = detector.detect(image)

#Desenați blob-uri pe imaginea noastră sub formă de cercuri roșii
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank,(0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#se ocupa cu numarare de cercuri si afisare lor
number_of_blobs = len(keypoints)
text = "Total Number of Blobs: "+ str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,0, 255),2)

#Afiseaza imaginea cu puncte cheie blob
cv2.imshow("Blobs using default parameters", blobs)
cv2.waitKey()

#Stabiliti parametri nostri de filtrare
#Initializati setarea parametrilor folosind cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

#Setati parametrii de filtrare a zonei
params.filterByArea = True #Activam functia
params.minArea = 100       #setam zona in care actineaza

#Setati parametrii de filtrare a circulatiei
params.filterByCircularity = True
params.minCircularity = 0.9

#Setati parametrii de filtrare a convexitatii
params.filterByConvexity = False
params.minConvexity = 0.2

#Stabiliți parametrii de filtrare a inerției
params.filterByInertia = True
params.minInertiaRatio = 0.01

#Creați un detector cu parametrii
detector = cv2.SimpleBlobDetector_create(params)

#detectare blobs
keypoints = detector.detect(image)

#Desenați blob-uri pe imaginea noastră sub formă de cercuri roșii
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image,keypoints,blank,(0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#se ocupa cu numarare de cercuri si afisare lor
number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,100,255),2 )

#Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey()
cv2.destroyAllWindows()

#Blob filtering -shape & Size
cv2.SimpleBlobDetector_Params()

######################################################################
#parametri pentru detecare
#Area
#+params.filterByArea = True/False
#+params.minArea = pixels
#+params.maxArea = pixels

#Circularity
#+ params.filterByCircularity = True/False
#+ params.minCircularity = 1 fiind un cerc perfect, 0 opusul

#Convexity-Zona blobului/Zona Convex Hull
#+params.filterByConvexity =True/False
#+params.minConvexity =0 to 1

#Inertia - Măsura elipticului (scăzut fiind mai eliptic, înalt fiind mai circular)
#params.filterByInertia = True/False
#params.minInertiaRatio =0,01
########################################################################
