import cv2
import numpy as np

# Dacă te întrebi de ce doar două dimensiuni, bine aceasta este o imagine în tonuri de gri, 
# Dacă facem o imagine colorată, vom folosi:
# rectangle = np.zeros((300, 300, 3),np.uint8)

#facem square
square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250), 255, -2)
cv2.imshow("Square", square)
cv2.waitKey()

#facem ellipse
ellipse = np.zeros((300,300), np.uint8)
cv2.ellipse(ellipse,(150,150), (150,150), 30, 0, 180, 255,-1)
cv2.imshow("Ellipse",ellipse)
cv2.waitKey()

cv2.destroyAllWindows()

#Experimentarea cu unele operațiuni BitWise

#arata unde ele se intersecteaza
And = cv2.bitwise_and(square,ellipse)
cv2.imshow("AND",And)
cv2.waitKey(0)

#Arată în cazul în care fie pătrat sau elipsă este 
bitwiseOr =cv2.bitwise_or(square, ellipse)
cv2.imshow('OR', bitwiseOr)
cv2.waitKey(0)

# Arată unde există de unul singur
bitwiseXor = cv2.bitwise_xor(square,ellipse)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

#Aratami tot ce nu este parte a Square
bitwiseNot_sq = cv2.bitwise_not(square)
cv2.imshow("NOT - square", bitwiseNot_sq)
cv2.waitKey(0)
cv2.destroyAllWindows()