import cv2

import numpy as np

def reducao_bicubica(img):
    #define o tamanho da altura e largura
    altura = img.shape[0]
    largura = img.shape[1]

    #cria uma nova matriz para nova imagem com tamanho reduzido em 3 vezes
    img_nova = np.zeros((int(altura/3), int(largura/3), img.shape[2]))

    #auxiliares para percorrer imagem nova
    aux_largura = 0
    aux_altura = 0 

    for i in range(0, int(altura/3)):
        aux_largura = 0
        for j in range(0, int(largura/3)):
            #separacao de soma para melhor manutenção
            # f(i,j) + f(i,j+1) + f(i,j+2)
            linha1 = img[aux_altura][aux_largura]+img[aux_altura][aux_largura+1]+img[aux_altura][aux_largura + 2]
            # f(i+1,j) + f(i+1,j+1)+ f(i+1,j+2)
            linha2 = img[aux_altura+1][aux_largura]+img[aux_altura+1][aux_largura+1]+img[aux_altura+1][aux_largura + 2]
            # f(i+2,j) + f(i+2,j+1)+ f(i+2,j+2)
            linha3 = img[aux_altura+2][aux_largura]+img[aux_altura+2][aux_largura+1]+img[aux_altura+2][aux_largura + 2]

            # (f(i,j) + f(i,j+1) + f(i,j+2) + f(i+1,j) + f(i+1,j+1)+ f(i+1,j+2) + f(i+2,j) + f(i+2,j+1)+ f(i+2,j+2))/9
            media_reducao = (linha1 + linha2 + linha3)/9  
            img_nova[i][j] = media_reducao

            #ajusta para pegar 3 casas após para reduzir de acordo
            aux_largura += 3
        aux_altura += 3

    return img_nova    

def ampliacao_bicubica(img):
    #define o tamanho da altura e largura
    altura = img.shape[0]
    largura = img.shape[1]

    #amplia o tamanho da matriz da nova imagem em 3 vezes
    n_largura = int(largura*3)
    n_altura = int(altura*3)

    #cria nova matriz vazia do tamanho dobrado da imagem anterior
    img_nova = np.zeros((n_altura, n_largura, img.shape[2]))

    #auxiliar para percorrer imagem
    aux_altura = 0
    aux_largura = 0

    for i in range(0, n_altura, 3):
        aux_largura = 0
        for j in range(0, n_largura, 3):
            #insere valores originais na nova matriz
            img_nova[i][j] = img[aux_altura][aux_largura]
            aux_largura += 1
        aux_altura += 1

    #preenche os espaços com calculo médio dos vizinhos mais próximo
    for i in range(0, n_altura - 3, 3):
        for j in range(0, n_largura - 3, 3):
            #a = (f(i,j) + f(i,j+1) + f(i,j+2)) / 3
            img_nova[i][j+1] = (img_nova[i][j] + img_nova[i][j+2] + img_nova[i][j+4])/3
            #b = (f(i,j) + f(i+1,j)+f(i+2,j) )/ 3
            img_nova[i+1][j] = (img_nova[i][j] + img_nova[i+2][j] + img_nova[i+4][j])/3 
            #c =  (f(i,j) + f(i,j+1) +f(i,j+2) + f(i+1,j) + f(i+1,j+1)+ f(i,j+2)+f(i+2,j+1) +f(i+2,j+2)+ f(i,j+2) + f(i+1,j+2)) / 9
            img_nova[i+1][j+1] = (
                img_nova[i][j] + img_nova[i][j+2] + img_nova[i][j+4] 
                + img_nova[i+2][j] + img_nova[i+2][j+2]+ img_nova[i+2][j+4] 
                + img_nova[i+4][j] + img_nova[i+4][j+2] +img_nova[i+4][j+4])/9
            #d =  (f(i,j+1) + f(i+1,j+1)+f(i+2,j+1)) /3
            img_nova[i+1][j+2] = (img_nova[i][j+2] + img_nova[i+2][j+2] + img_nova[i+4][j+2])/3
            #e = (f(i+1,j) + f(i+1,j+1)) / 2  
            img_nova[i+2][j+1] = (img_nova[i+2][j] + img_nova[i+2][j+2] + img_nova[i+2][j+4])/3

    return img_nova

def main():
    #lê imagem e reduz ela e salva em variavel
    imagem = cv2.imread('imagens\cubo.png')
    img_reduzida = reducao_bicubica(imagem)
    img_ampliada = ampliacao_bicubica(imagem)

    #gera nova imagem 
    cv2.imwrite('./imagens/cubo_reduzido_bicubica.png', img_reduzida)
    cv2.imwrite('./imagens/cubo_ampliado_bicubica.png', img_ampliada)

if __name__ == '__main__':
    main()
        