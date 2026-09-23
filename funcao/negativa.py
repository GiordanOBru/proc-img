import cv2

import numpy as np

def negativa(img):
    #define o tamanho da imagem
    altura = img.shape[0]
    largura = img.shape[1]

    #matriz nova para negativa
    img_negativa = np.zeros((altura, largura), dtype=np.uint8)

    #Soma simples entre pixels 
    for i in range(altura - 1):
        for j in range(largura - 1):
            #analisa pixel e transforma em negativo
            pixel_positivo = img[i,j]
            pixel_negativo = 255 - pixel_positivo

            img_negativa [i,j] = pixel_negativo

    return img_negativa

def main():
    #lê imagem e deixa em tons de cinza
    imgB = cv2.imread('imagens/imgB.png', cv2.IMREAD_GRAYSCALE)
    img_negativa = negativa(imgB)

    #gera nova imagem negativa
    cv2.imwrite('./imagens/negativa.png', img_negativa)

if __name__ == '__main__':
    main()