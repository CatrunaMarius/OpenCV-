import cv2
import numpy as np

#incarca imaginea
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\Sunflowers.jpg", cv2.IMREAD_GRAYSCALE)

#Configureaza detectorul cu parametrii prestabiliti
detector = cv2.SimpleBlobDetector_create()

#detectati blobs
keypoints = detector.detect(image)

#Desenati detector blobs ca cercuri rosii
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS asigura dimensiunea
#cercului corespunzator dimensiunii blobului
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image,keypoints,blank,(0,0,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

#arata keypoints
cv2.imshow("Blobs", blobs)
cv2.waitKey()
cv2.destroyAllWindows()

#Funcția cv2.drawKeypoints are următoarele argumente:

#cv2.drawKeypoints (imagine de intrare, puncte cheie, blank_output_array, culoare, steaguri)

#steaguri:

#cv2.DRAW_MATCHES_FLAGS_DEFAULT
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
#cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
#cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS