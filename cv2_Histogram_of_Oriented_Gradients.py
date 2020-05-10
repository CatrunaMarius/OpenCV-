import numpy as np
import matplotlib.pyplot as plt
import cv2

#Incaraca imaginea si converteste in alb si negru
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\elephant.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Arata imaginea originala
cv2.imshow("Input Image", image)
cv2.waitKey()

#h x w in pixeli
cell_size = (8, 8)#defini dimensiunea pixelurilor

#h x w in cells
block_size = (2, 2)#normailzam blocuri

#numarul de cosuri de orientare
nbins =9

#Utilizarea descriptorului HOG al OpenCv
#winSize este dimensiunea imaginii decupata la un multiolu al dimensiuni celulei
hog = cv2.HOGDescriptor(_winSize=(gray.shape[1] // cell_size[1]*cell_size[1],
                                  gray.shape[0] // cell_size[0]*cell_size[0]),
                       _blockSize=(block_size[1] * cell_size[1],
                                   block_size[0] * cell_size[0]),
                       _blockStride=(cell_size[1], cell_size[0]),
                       _cellSize=(cell_size[1], cell_size[0]),
                       _nbins=nbins)

#Crem o forma de matrice numpay pe care o folosim pt a crea hog_feats
n_cells = (gray.shape[0] // cell_size[0], gray.shape[1] // cell_size[1])

#Mai intai indexam blocurile pe randuri
#hot_feats contine acum amplitudinile gradientului pe fiecare direectie,
#pt fiecare celula a grupului  pt fiecare grupa. Indexarea se face pe randuri si apoi pe coloane
hog_feats = hog.compute(gray).reshape(n_cells[1] - block_size[1] + 1,
                                      n_cells[0] - block_size[0] +1,
                                      block_size[0], block_size[1], nbins).transpose((1,0,2,3,4))

#Creati tabloul de gradatii cu dimensiuni nbin pt a stoca orientari de gradient
gradients = np.zeros((n_cells[0],n_cells[1],nbins))

#Creati o serie de dimensiuni
cell_count = np.full((n_cells[0],n_cells[1], 1),0, dtype=int)

#Normalizarea blocurilor

for off_y in range(block_size[0]):
    for off_x in range(block_size[1]):
        gradients[off_y:n_cells[0] - block_size[0] + off_y +1,
                  off_x:n_cells[1] - block_size[1] + off_x +1] += \
                      hog_feats[:, :, off_y, off_x, :]
        cell_count[off_y:n_cells[0] - block_size[0] + off_y +1,
                   off_x:n_cells[1] - block_size[1] + off_x +1] +=1

#Gradienti medii
gradients /= cell_count

#Plot HOG foloseste Matplotlib
#unghiul este 360 / nbins * directie
color_bins =5
plt.pcolor(gradients[:, :, color_bins])
plt.gca().invert_yaxis()
plt.gca().set_aspect("equal", adjustable='box')
plt.colorbar()
plt.show()
cv2.destroyAllWindows()

#HOG-urile sunt descriptor de caracteristici care a fost utilizat pe scară largă și cu succes pentru detectarea obiectelor.

#Reprezintă obiectele ca un singur vector caracteristic, spre deosebire de un set de vectori caracteristici în care fiecare reprezintă un segment al imaginii.

#Este calculat prin detectarea ferestrei glisante peste o imagine, unde un descriptor HOG este calculat pentru fiecare poziție. Ca SIFT, scara imaginii este reglată (piramidă)

#HOG-urile sunt deseori utilizate cu clasificatoarele SVM (vector vector support). Fiecare descriptor HOG care este calculat este transmis unui clasificator SVM pentru a determina id-ul obiectului a fost găsit sau nu)

#Great Peper de Dalal & Triggs privind utilizarea HOG-urilor pentru detectarea oamenilor:
#https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf

#HOG pas cu pas
#1.Folosind o fereastră sau o celulă de detectare a pixelilor de 8x8 (în verde) calculăm vectorul de gradient sau orientările de margine la fiecare pixel.

#2.Acesta generează 64 (8x8) vectori gradient, care sunt apoi reprezentați ca o histogramă.

#3.Fiecare celulă este apoi împărțită în  unghiuri bins(cosuri), unde fiecare bin(coș)  corespunde unei direcții de gradient (de exemplu, x, y). În hârtia Delal și Triggs au folosit 9 bins(coșuri) 0-180 (20 fiecare bin(coș)).

#4.Aceasta reduce efectiv 64 de vectori la doar 9 valori.

#5.Deoarece păstrează mărimile gradienților, este relativ imun la deformări.

#6.Apoi Normalizăm gradienții pentru a asigura invarianța la schimbări de iluminare, adică Luminozitate și Contrast. De exemplu. în imaginile din dreapta dacă împărțim vectorii în funcție de mărimea gradientului obținem 0,707 pentru toți, aceasta este normalizarea.

#7.Instaurați normalizarea inviduală a celulelor ferestrei, se utilizează o metodă numită Normalizare bloc. Acest lucru ține cont de blocurile vecine, astfel încât normalizăm luând în considerare segmente mai mari ale imaginii
 