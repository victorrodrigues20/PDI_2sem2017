import cv2

pathImagem = 'D:\\GitHub\\PDI_2sem2017\\Imagens\\urso.jpg'

img = cv2.imread(pathImagem)
#height, width, channels = img.shape
#print(height, width, channels, img.size)
#print(img.shape, img.size)


# CV_8U, CV_16U, CV_32F, COLOR_RGB2GRAY
small = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(small.shape, small.size)

'''
CV_8U
(320, 450, 3) 432000
(320, 450, 4) 576000

CV_16U
(320, 450, 3) 432000
(320, 450, 4) 576000

CV_32F
(320, 450, 3) 432000
(320, 450, 4) 576000

COLOR_RGB2GRAY
(320, 450, 3) 432000
(320, 450) 144000

'''

cv2.imshow("Imagem1", img)
cv2.imshow("Imagem2", small)

cv2.waitKey(0)
cv2.destroyAllWindows()