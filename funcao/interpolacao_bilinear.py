import cv2

import numpy as np

def reducao_bilinear(img):
    #define o tamanho da altura e largura
    altura = img.shape[0]
    largura = img.shape[1]

    #cria uma nova matriz para nova imagem com tamanho reduzido em 2 vezes
    img_nova = np.zeros((int(altura/2), int(largura/2), img.shape[2]))

    #auxiliares para percorrer imagem nova
    aux_largura = 0
    aux_altura = 0 

    for i in range(0, int(altura/2)):
        aux_largura = 0
        for j in range(0, int(largura/2)):
            #pega 4 pixels ao redor soma e faz a média
            # f(i,j) +f(i,j+1) 
            linha1 = img[aux_altura][aux_largura]+img[aux_altura][aux_largura+1]
            # f(i+1,j) + f(i+1,j+1)
            linha2 = img[aux_altura+1][aux_largura]+img[aux_altura+1][aux_largura+1]

            # (f(i,j) + f(i,j+1) + f(i+1,j) + f(i+1,j+1))/4           
            media_reducao = (linha1+linha2)/4
            img_nova[i][j] = media_reducao

            #ajusta para pegar 2 casas após para reduzir de acordo
            aux_largura += 2
        aux_altura += 2

    return img_nova    

def ampliacao_bilinear(img):
    #define o tamanho da altura e largura
    altura = img.shape[0]
    largura = img.shape[1]

    #amplia o tamanho da matriz da nova imagem em 2 vezes
    n_largura = int(largura*2)
    n_altura = int(altura*2)

    #cria nova matriz vazia do tamanho dobrado da imagem anterior
    img_nova = np.zeros((n_altura, n_largura, img.shape[2]))

    #auxiliar para percorrer imagem
    aux_altura = 0
    aux_largura = 0

    for i in range(0, n_altura, 2):
        aux_largura = 0
        for j in range(0, n_largura, 2):
            #insere valores originais na nova matriz
            img_nova[i][j] = img[aux_altura][aux_largura]
            aux_largura += 1
        aux_altura += 1

    #preenche os espaços com calculo médio dos vizinhos mais próximo
    for i in range(0, n_altura - 2, 2):
        for j in range(0, n_largura - 2, 2):
            #a = (f(i,j) + f(i,j+1)) / 2
            img_nova[i][j+1] = (img_nova[i][j] + img_nova[i][j+2])/2
            #b = (f(i,j) + f(i+1,j)) / 2
            img_nova[i+1][j] = (img_nova[i][j] + img_nova[i+2][j])/2
            #c = (f(i,j) + f(i,j+1) + f(i+1,j) + f(i+1,j+1)) / 4 
            img_nova[i+1][j+1] = (img_nova[i][j] + img_nova[i][j+2] + img_nova[i+2][j] + img_nova[i+2][j+2])/4
            #d = (f(i,j+1) + f(i+1,j+1)) / 2
            img_nova[i+1][j+2] = (img_nova[i][j+2] + img_nova[i+2][j+2])/2
            #e = (f(i+1,j) + f(i+1,j+1)) / 2  
            img_nova[i+2][j+1] = (img_nova[i+2][j] + img_nova[i+2][j+2])/2

    return img_nova

def main():
    #lê imagem e reduz ela e salva em variavel
    imagem = cv2.imread('imagens\cubo.png')
    img_reduzida = reducao_bilinear(imagem)
    img_ampliada = ampliacao_bilinear(imagem)

    #gera nova imagem 
    cv2.imwrite('./imagens/cubo_reduzido_bilinear.png', img_reduzida)
    cv2.imwrite('./imagens/cubo_ampliado_bilinear.png', img_ampliada)

if __name__ == '__main__':
    main()
        