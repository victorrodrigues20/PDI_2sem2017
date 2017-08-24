import cv2

pathImagem = 'D:\\GitHub\\PDI_2sem2017\\Imagens\\urso.jpg'

img = cv2.imread(pathImagem)

height, width, channels = img.shape
print(height, width, channels, img.size)

small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

height, width, channels = small.shape
print(height, width, channels, small.size)

cv2.imshow("Imagem1", img)
cv2.imshow("Imagem2", small)

cv2.waitKey(0)
cv2.destroyAllWindows()
