# PROCESSAMENTO DE IMAGEM

## Ampliação e Redução

São utilizados três métodos para alterar a resolução das imagens:

* **Vizinho mais próximo:** utiliza o valor do pixel mais próximo. É simples e rápido, mas pode deixar a imagem pixelada.
* **Interpolação bilinear:** utiliza os pixels vizinhos para calcular valores intermediários, produzindo uma imagem mais suave.
* **Interpolação bicúbica:** considera uma quantidade maior de pixels vizinhos, proporcionando maior suavidade e qualidade, porém com maior custo computacional.

## Operações Aritméticas

As operações aritméticas são realizadas **pixel a pixel** e, normalmente, exigem imagens com as mesmas dimensões.

### Adição

\(s(x,y) = f(x,y) + g(x,y)\)

Utilizada para:

* Combinar ou fundir imagens;
* Reduzir ruídos por meio da média de várias imagens;
* Realçar informações presentes em diferentes imagens.

Em imagens de 8 bits, pode ser necessário realizar o **escalamento ou a média** para evitar valores acima de 255.

### Subtração

\(d(x,y) = f(x,y) - g(x,y)\)

Utilizada para:

* Destacar diferenças entre imagens;
* Detectar alterações entre frames;
* Evidenciar estruturas em aplicações médicas, como na angiografia por subtração digital.

## Transformação Negativa de Intensidade

A **transformação negativa** inverte os níveis de intensidade de cada pixel da imagem.

### Fórmula

\(s = (L - 1) - r\)

Onde:

* **$r$:** intensidade original do pixel;
* **$s$:** nova intensidade do pixel;
* **$L$:** quantidade de níveis de intensidade da imagem.

Para imagens de 8 bits:

\(s = 255 - r\)

A transformação converte **tons claros em escuros e tons escuros em claros**, sendo útil para destacar detalhes claros presentes em regiões predominantemente escuras.

## Equalização de Histograma

A **equalização de histograma** é uma técnica utilizada para redistribuir os níveis de intensidade de uma imagem, aumentando o **contraste global** e destacando detalhes.

### Etapas do Algoritmo

1. **Histograma:** conta a quantidade de ocorrências de cada nível de cinza.
2. **Probabilidade:** calcula a frequência normalizada de cada nível:

\(p_r(r_k) = \frac{n_k}{n}\)

Onde $n_k$ é a quantidade de pixels no nível de cinza $k$ e $n$ é o total de pixels da imagem.

3. **Frequência acumulada (CDF):** soma as probabilidades dos níveis de cinza de forma acumulada.
4. **Look-Up Table (LUT):** utiliza a CDF para determinar o novo valor de cada nível de cinza:

\(LUT[k] = round\left((L - 1) \times CDF[k]\right)\)

5. **Mapeamento:** substitui cada pixel da imagem original pelo valor correspondente na **LUT**, gerando a imagem com o histograma equalizado.

## Operações Geométricas

As transformações geométricas alteram a **posição ou a dimensão dos pixels**, mapeando as coordenadas da imagem original para novas posições.

O mapeamento pode ser:

* **Direto:** leva os pixels da imagem original para a imagem de saída, podendo gerar espaços vazios ou sobreposições.
* **Inverso:** parte da imagem de saída e utiliza a transformação inversa para encontrar os pixels correspondentes na imagem original.

### Principais Transformações

* **Translação:** desloca a imagem nos eixos X e Y.
* **Escala:** amplia ou reduz a imagem.
* **Rotação:** gira a imagem em torno de um ponto.
* **Espelhamento (Flip):** inverte a imagem horizontal ou verticalmente.
* **Cisalhamento (Shear):** inclina ou deforma a imagem horizontal ou verticalmente.

As transformações geométricas podem utilizar **interpolação** para determinar os valores dos pixels que surgem durante o processo.
