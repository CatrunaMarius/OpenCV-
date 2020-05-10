import cv2
import numpy as np

#avem nevoie sa importam matplatlib pentru a crea histograme
from matplotlib import pyplot as plt

imaginea = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg')
histogram = cv2.calcHist([imaginea], [0], None, [256],[0,256])
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist, accumulate])
#imaginea : este imaginea sursă de tip uint8 sau float32. trebuie indicat între paranteze pătrate, adică „img”.
#canale: se administrează și între paranteze pătrate. Este indicele canalului pentru care calculăm histograma. De exemplu, dacă intrarea este o imagine la scară gri, valoarea acesteia este 0. Pentru imaginea color, puteți trece 0, 1 sau 2 pentru a calcula histograma canalului albastru, verde sau roșu respectiv.
#mască: mască imagine. Pentru a găsi o histogramă a imaginii complete, aceasta este dată ca „None”. Dar dacă doriți să găsiți o histogramă a unei anumite regiuni de imagine, trebuie să creați o imagine de mască pentru asta și să o dați ca mască. (Voi arăta un exemplu mai târziu.)
#histSize: aceasta reprezintă numărul nostru BIN. Trebuie să fie prezentate între paranteze pătrate. Pentru scara completă, trecem 256.
#range: aceasta este GAMA noastră. În mod normal, este 0,256.


#we plot a histogram, ravel() flatens our image array
plt.hist(imaginea.ravel(), 256, [0,256]); plt.show()#pt vizualizare


#vizualizare separata a calaleor de culoare
color = ('b', 'g', 'r')

#acum sepărăm culorile și plot fiecare în Histogramă

for i,col in enumerate(color):
    histogram2 = cv2.calcHist([imaginea], [i], None, [256],[0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])
plt.show() 

# o alta imagine
imaginea = cv2.imread('D:\Programare\cv\Master OpenCV\images\Tobago.jpg')
histogram = cv2.calcHist([imaginea], [0], None, [256],[0,256])

#we plot a histogram, ravel() flatens our image array
plt.hist(imaginea.ravel(), 256, [0,256]); 
plt.show()#pt vizualizare


#vizualizare separata a calaleor de culoare
color = ('b', 'g', 'r')

#acum sepărăm culorile și plot fiecare în Histogramă

for i,col in enumerate(color):
    histogram2 = cv2.calcHist([imaginea], [i], None, [256],[0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])
plt.show()