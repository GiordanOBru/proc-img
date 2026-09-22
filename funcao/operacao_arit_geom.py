import cv2

import numpy as np

def adicao_aritmetica(imgA, imgB):
    #define o tamanho da imagem
    altura = 260
    largura = 260

    #transformando imgs no mesmo tamanho
    imgA = cv2.resize(imgA, (largura, altura))
    imgB = cv2.resize(imgB, (largura, altura))

    #matriz resultante da soma
    img_soma = np.zeros((altura, largura), dtype=np.uint8)

    #Soma simples entre pixels 
    for i in range(altura):
        for j in range(largura):
            img_soma[i,j] = int((float(imgA[i,j])+float(imgB[i,j]))/2)

    return img_soma

def subtracao_aritmetica(imgA, imgB):
    #define o tamanho da imagem
    altura = 260
    largura = 260

    #transformando imgs no mesmo tamanho
    imgA = cv2.resize(imgA, (largura, altura))
    imgB = cv2.resize(imgB, (largura, altura))

    #matriz resultante da soma
    img_sub = np.zeros((altura, largura), dtype=np.uint8)

    #Soma simples entre pixels 
    for i in range(altura):
        for j in range(largura):
            conferencia = int((float(imgA[i,j])-float(imgB[i,j]))/2)
            if (conferencia) < 0 :
                img_sub[i,j] = 0
            else:
                img_sub[i,j] = conferencia

    return img_sub

def operacao_geo_reflexao(img):
    #define tamanho da imagem
    altura = 260
    largura = 260

    #transformando imgs no mesmo tamanho
    img_nova  = cv2.resize(img,(largura, altura))

    #matriz resultante da inversão
    img_geo = np.zeros((altura, largura), dtype=np.uint8)

    #inversao da imagem
    for i in range(0, altura - 1):
        for j in range(0, largura -1):
            largura_inversa = (largura - 1) - j
            img_geo[i][largura_inversa] = img_nova[i][j]

    return img_geo


def main():
    #lê imagem e reduz ela e salva em variavel
    imgA = cv2.imread('imagens\imgA.png', cv2.IMREAD_GRAYSCALE)
    imgB = cv2.imread('imagens\imgB.png', cv2.IMREAD_GRAYSCALE)
    img_soma = adicao_aritmetica(imgA, imgB)
    img_sub = subtracao_aritmetica(imgA, imgB)
    img_geo = operacao_geo_reflexao(imgA)

    #gera novas imagens 
    cv2.imwrite('./imagens/soma.png', img_soma)
    cv2.imwrite('./imagens/subtracao.png', img_sub)
    cv2.imwrite('./imagens/geo.png', img_geo)

if __name__ == '__main__':
    main()