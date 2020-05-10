import cv2
import numpy as np

image =cv2.imread("D:\Programare\cv\Master OpenCV\images\elephant.jpg")
cv2.imshow('Original Image', image)
cv2.waitKey()

#cream 3 x 3 kernel
kernel_3x3 = np.ones((3,3), np.float32)/9

# Folosim cv2.fitler2D pentru a conovlve kernal cu o imagine
blurred = cv2.filter2D(image, -1,kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred)
cv2.waitKey()

#cream un kernel 7 x 7
kernel_7x7 = np.ones((7,7),np.float32)/49

blurred2 = cv2.filter2D(image,-1,kernel_7x7)
cv2.imshow('7x7 Kernel Blurring',blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Other commonly used blurring methods in OpenCV

image =cv2.imread("D:\Programare\cv\Master OpenCV\images\elephant.jpg")

# Averaging făcut prin convolving imaginea cu un filtru de cutie normalizat. 
# Acest lucru ia pixeli sub cutie și înlocuiește elementul central
# Mărimea cutiei trebuie să fie ciudată și pozitivă 

blur = cv2.blur(image,(3,3))
cv2.imshow('Averaging', blur)
cv2.waitKey(0)

## În loc de filtru cutie, kernel Gaussian
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

# Takes median of all the pixels under kernel area and central 
# element is replaced with this median value
median =cv2.medianBlur(image,5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# Bilateral este foarte eficient în îndepărtarea zgomotului păstrând marginile ascuțite
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image De-noising - Non-Local Means Denoising


image =cv2.imread("D:\Programare\cv\Master OpenCV\images\elephant.jpg")

# Parametrii, după nici unul sunt-puterea filtrului ' h ' (5-10 este o gamă bună)
# Next este hForColorComponents, setat ca aceeași valoare ca h din nou

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6,7,21)

cv2.imshow('Fast Means Denoising', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Există 4 variante de mijloace non-locale care denota:

#cv2.fastNlMeansDenoising ()-funcționează cu o singură imagine în tonuri de gri
#cv2.Fastnlmeansdenoisingcolorate ()-funcționează cu o imagine color.
#cv2.fastNlMeansDenoisingMulti ()-funcționează cu secvențe de imagini capturate într-o perioadă scurtă de timp (imagini în tonuri de gri)
#cv2.fastNlMeansDenoisingColoredMulti ()-la fel ca mai sus, dar pentru imagini color.