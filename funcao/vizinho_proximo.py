import cv2

import numpy as np

def reducao_vizinho(img):
    #define o tamanho da altura e largura
    largura = img.shape[0]
    altura = img.shape[1]

    #cria uma nova matriz para nova imagem com tamanho reduzido em 2 vezes
    img_nova = np.zeros((int(largura/2), int(altura/2), img.shape[2]))

    #auxiliares para percorrer imagem nova
    aux_largura = 0
    aux_altura = 0 

    
    for i in range(0, int(largura/2)):
        aux_largura = 0
        for j in range(0, int(altura/2)):
            #copia o pixel da imagem original na nova imagem,
            img_nova[i][j] = img[aux_altura][aux_largura]
            #ajusta para pegar 2 casas após para reduzir de acordo
            aux_largura += 2
        aux_altura += 2

    return img_nova    

def ampliacao_vizinho(img):
    #define o tamanho da altura e largura
    largura = img.shape[0]
    altura = img.shape[1]

    #amplia o tamanho da matriz da nova imagem em 2 vezes
    n_largura = int(largura*2)
    n_altura = int(altura*2)

    #cria nova matriz vazia do tamanho dobrado da imagem anterior
    img_nova = np.zeros((n_largura, n_altura, img.shape[2]))

    #auxiliar para percorrer imagem
    aux_largura = 0
    aux_altura = 0

    for i in range(0, n_largura, 2):
        aux_largura = 0
        for j in range(0, n_altura, 2):
            #insere valores originais na nova matriz
            img_nova[i][j] = img[aux_altura][aux_largura]
            aux_largura += 1
        aux_altura += 1

    #preenche os espaços com o vizinho mais próximo
    for i in range(0, n_largura - 1, 2):
        for j in range(0, n_altura - 1, 2):
            #repete o pixel em 4 posições
            img_nova[i][j+1] = img_nova[i][j]
            img_nova[i+1][j] = img_nova[i][j]
            img_nova[i+1][j+1] = img_nova[i][j]

    return img_nova

def main():
    #lê imagem e reduz ela e salva em variavel
    imagem = cv2.imread('imagens\cubo.png')
    img_reduzida = reducao_vizinho(imagem)
    img_ampliada = ampliacao_vizinho(imagem)

    #gera nova imagem 
    cv2.imwrite('./imagens/cubo_reduzido.png', img_reduzida)
    cv2.imwrite('./imagens/cubo_ampliado.png', img_ampliada)

if __name__ == '__main__':
    main()
        