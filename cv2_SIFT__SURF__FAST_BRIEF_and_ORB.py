
#Algoritmii SIFT si SURF sunt brevetati de creatorii respectivi si desi sunt liberi de ai folosi in setari academince si de cercetare , ar trebui sa obtineti din punct de vedere tehnic o licenta/ permisiunea creatorilor daca le utilizati in comert (adica cu scop lucrativ)

import cv2
import numpy as np

#image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

##creati obiectul SIFT Featur Detector
#sift =cv2.xfeatures2d_SIFT


##detectare punctelor cheie
#keypoints = sift.detect(gray, None)
#print("Number of keypoints Detected: ", len(keypoints))

##Desenati punctel cheie bogate pe imaginea de intrare
#image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imshow("Fature Method - SIFT", image)
#cv2.waitKey()
#cv2.destroyAllWindows()









#SURF

#image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

##Creaza SURF Feature Detector object
#surf = cv2.SURF()

##doar functiile al caror hessian este mai mare decat hessian, pragul este retinut de detector
#surf.hessianThreshold = 500
#keypoints,descriptors = surf.detectAndCompute(gray,None)
#print("Number of keypoints Detected: ", len(keypoints))

##Desenati punctel cheie bogate pe imaginea de intrare
#image = cv2.drawKeypoints(image,keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imshow("Feature Method - SURF", image)
#cv2.waitKey()
#cv2.destroyAllWindows()








#FAST

#image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

##Creare FAST Detecor object
#fast = cv2.FastFeatureDetector()

##Optine punctele cheie, in mod implicit, suprimarea non max este activata
##pt a dezactiva setul fast.setBool('nonmaxSUppression', False)
#kaypoints = fast.detect(gray, None)
#print("Number of keypoints Detected: ", len(keypoints))

##Desenati punctel cheie bogate pe imaginea de intrare
#image = cv2.drawKeypoints(image,kaypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imshow("Feature Method - FAST", image)
#cv2.waitKey()
#cv2.destroyAllWindows()






#BRIEF

#image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

##Creare FAST detector object
#star = cv2.FeatureDetector_create("STAR")

##Create BRIEF extragere object
#brief = cv2.DescriptorExtractor_create("BRIEF")

##Determina punctele cheie
#keypoints = star.detect(gray, None)

##Obtineti descriptori si noi puncte cheie dinale utilizand BRIEF
#keypoints, descriptors = brief.compute(gray, keypoints)
#print("Number of keypoints Detected: ", len(keypoints))

##Desenati punctel cheie bogate pe imaginea de intrare
#image = cv2.drawKeypoints( image,keypoint, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imshow("Feature Method - BRIEF", image)
#cv2.waitKey()
#cv2.destroyAllWindows()


  




#Oriented FAST and Rotated BRIEF (ORB)

image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Creati obiect ORB, putem specifica numarul de puncte cheie pe care le dorim
orb = cv2.ORB_create()

#Determina punctele cheie
keypoints, descriptors = orb.detectAndCompute(gray, None)

#Obtine descripori
print("Number of keypoints Detected: ",len(keypoints))

#Desenati punctele cheie bogate in imaginea de intrare
image = cv2.drawKeypoints(image,keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Feature Method - ORB", image)
cv2.waitKey()
cv2.destroyAllWindows()
