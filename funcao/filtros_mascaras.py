import cv2

import numpy as np
import math

MASCARALAPLACIANO_1 = np.array([
    [0,1,0],
    [1,-4,1],
    [0,1,0]
])

MASCARALAPLACIANO_2 = np.array([
    [1,1,1],
    [1,-8,1],
    [1,1,1]
])

MASCARALAPLACIANO_3 = np.array([
    [0,-1,0],
    [-1,4,-1],
    [0,-1,0]
])

MASCARALAPLACIANO_4 = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
])

SOBELX = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
])

SOBELY = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
])

def filtro_laplaciano(img, MASCARA):
    #define o tamanho da imagem
    altura = img.shape[0]
    largura = img.shape[1]

    #criando matriz vazia
    img_filtrada_laplaciano = np.zeros((altura, largura), dtype=np.uint8)

    #ignora as bordas e percorre a imagem
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            soma = 0

            for m in range(-1,2):
                for n in range(-1,2):
                    soma += img[i+m, j+n] * MASCARA[m+1, n+1]

            if soma < 0:
                soma = 0 

            elif soma > 255:
                soma = 255             

            img_filtrada_laplaciano[i,j] = soma
         
    return img_filtrada_laplaciano

def filtro_sobel(img):
    #define o tamanho da imagem
    altura = img.shape[0]
    largura = img.shape[1]

    #criando matriz vazia
    img_filtrada_sobel = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura - 2):
        for j in range(largura - 2):
            suporte_i = 0
            suporte_j = 0

            #aplicacao mascara
            for k in range(-1,2):
                for l in range(-1,2):
                    suporte_i += img[i+k, j+l] * SOBELX[k+1, l+1]
                    suporte_j += img[i+k, j+l] * SOBELY[k+1, l+1]

            #magnitude gradiente
            magnitude = math.sqrt((suporte_i * suporte_i) + (suporte_j* suporte_j))

            if magnitude > 255:
                magnitude = 255

            img_filtrada_sobel[i,j] = magnitude

    return img_filtrada_sobel

def main():
    #definição das mascaras laplacianas
    mascaras = [MASCARALAPLACIANO_1, MASCARALAPLACIANO_2,
                MASCARALAPLACIANO_3, MASCARALAPLACIANO_4]

    #lê imagem na escala cinza
    imgA = cv2.imread('imagens/imgA.png', cv2.IMREAD_GRAYSCALE)
    for i in range(len(mascaras)):
        imgLaplaciano = filtro_laplaciano(imgA, mascaras[i])
        cv2.imwrite(f'./imagens/filtro_laplaciano_{i+1}.png', imgLaplaciano)

    imgSobel = filtro_sobel(imgA)
    cv2.imwrite(f'./imagens/filtro_sobel.png', imgSobel)

if __name__ == '__main__':
    main()