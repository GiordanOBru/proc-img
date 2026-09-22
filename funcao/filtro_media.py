import cv2

import numpy as np

def filtro_media(img):
    #define o tamanho da imagem
    altura = img.shape[0]
    largura = img.shape[1]

    #criando imagem com bordas igual a 0
    img_com_bordas = np.zeros((altura + 2, largura + 2), dtype=np.uint8)
    img_filtro_media = np.zeros((altura, largura), dtype=np.uint8)

    #insere img original em img_com_bordas
    for i in range(altura):
        for j in range(largura):
            img_com_bordas [i + 1, j + 1] = img[i,j]

    #aplica mascara 3x3
    for i in range(altura):
        for j in range(largura):
            soma = 0

            for k in  range(-1,2):
                for l in range(-1,2):
                    soma += img_com_bordas[(i+1)+ k,(j+1)+l]

            img_filtro_media[i,j] = soma // 9

    return img_filtro_media

def main():
    #lê imagem na escala cinza
    imgA = cv2.imread('imagens\cubo.png', cv2.IMREAD_GRAYSCALE)
    img_filtro_media = filtro_media(imgA)

    #gera nova imagem com filtro medio
    cv2.imwrite('./imagens/filtro_media.png', img_filtro_media)

if __name__ == '__main__':
    main()