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
