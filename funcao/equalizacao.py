import cv2

import numpy as np

def equalizacao(img, nivel):
    #inserindo nível de cinza conforme main
    if nivel != 256:
        fator = 256 // nivel
        img =  (img // fator).astype(np.uint8)

    nivel_cinza = nivel

    #definindo histograma e ajuste_final
    histograma = [0] * nivel_cinza
    ajuste_final = [0] * nivel_cinza

    #define o tamanho da imagem
    altura = img.shape[0]
    largura = img.shape[1]

    #matriz nova para equalizar
    img_equalizada = np.zeros((altura, largura), dtype=np.uint8)

    #contando tons existentes no histograma
    for i in range(altura):
        for j in range(largura):
            tom = img[i,j]
            histograma[tom] += 1

    #declarando as variaveis utilizadas mais tarde
    freq_acumulada = 0
    quantidade_total = altura*largura

    #Aplica a fórmula (L - 1) * freq_acumulada arredondado
    for i in range(nivel_cinza):
        probabilidade = histograma[i]/quantidade_total
        freq_acumulada += probabilidade
        ajuste_final[i] = round((nivel_cinza-1)*freq_acumulada)

    #finalizando equalização
    for i in range(altura):
        for j in range(largura):
            img_equalizada[i,j] = ajuste_final[img[i,j]]

    #ajuste de escala de acordo nível reduzido
    if nivel != 256:
        fator = 255 // (nivel - 1)
        img_equalizada = (img_equalizada * fator).astype(np.uint8)

    return img_equalizada

def main():
    #lê imagem e deixa em tons de cinza
    #8,16,32,64,128,256...8 em 8 bits
    nivel = 128
    imgA = cv2.imread('imagens/imgA.png', cv2.IMREAD_GRAYSCALE)
    img_equalizada = equalizacao(imgA, nivel)

    #gera nova imagem equalizada
    cv2.imwrite('./imagens/equalizacao_'+str(nivel)+'.png', img_equalizada)

if __name__ == '__main__':
    main()