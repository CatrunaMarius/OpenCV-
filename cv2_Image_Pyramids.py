import cv2
#Useful when scaling images in object detection.

image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow('Original', image)

cv2.imshow('Smaller', smaller)
cv2.imshow('Larger', larger)
cv2.waitKey()
cv2.destroyAllWindows()
