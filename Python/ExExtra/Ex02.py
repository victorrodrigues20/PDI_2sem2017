import cv2
from matplotlib import pyplot as plt

# Lê imagem
image = cv2.imread('../../imagens/pecasLego.jpg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Armazena cada canal da imagem RGB em 3 variáveis (R, G e B)
H, S, V = cv2.split(hsv_image)

merged = cv2.merge([H, S, V+15])


# Criação de um vetor representando cada canal da imagem RGB
color = ('b','g','r')

rgbMerged = cv2.cvtColor(merged, cv2.COLOR_HSV2BGR)

# FOR em cada canal
for i,col in enumerate(color):
    histr = cv2.calcHist([rgbMerged],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

cv2.waitKey(0)


cv2.imshow("Imagem Normal", image)
cv2.imshow("HSV ampliado", rgbMerged)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# Junta todos os canais em 1 imagem só: (R, G e B) para (RGB)
merged = cv2.merge([B, G, R])

# Exibe a imagem (título da janela, imagem)
cv2.imshow("Merge", merged)

# Adiciona 100 apenas no canal Blue (processo de Amplificação)
merged = cv2.merge([B, G, R])

# Exibe imagem com canal Azul amplificado
cv2.imshow("Merge com Amplificação canal Azul", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''