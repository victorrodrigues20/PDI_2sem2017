import cv2
import numpy as np
from matplotlib import pyplot as plt

# Ler documentação oficinal:
# http://docs.opencv.org/trunk/d1/db7/tutorial_py_histogram_begins.html

pathImagem = 'D:\\GitHub\\PDI_2sem2017\\Imagens\\urso.jpg'

img = cv2.imread(pathImagem)
color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
