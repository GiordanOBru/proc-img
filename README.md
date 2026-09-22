# PROCESSAMENTO DE IMAGEM

## Ampliação e Redução

Nessa primeira etapa, a imagem será organizada utilizando diferentes métodos de ampliação e redução: **vizinho mais próximo, interpolação bilinear e interpolação bicúbica**.

**Vizinho mais próximo:** pega o valor do pixel mais próximo e replica esse valor para preencher os novos pixels. É um método simples e rápido, mas pode deixar a imagem mais pixelada.

**Interpolação bilinear:** considera os pixels vizinhos e calcula o novo valor a partir deles, utilizando uma média ponderada. Na ampliação, utiliza os pixels mais próximos para gerar valores intermediários, deixando a imagem mais suave.

**Interpolação bicúbica:** considera uma quantidade maior de pixels vizinhos para calcular o novo valor, proporcionando uma imagem mais suave e com melhor qualidade. É mais complexa e exige mais processamento que os métodos anteriores.

## Operação Aritmética

As operações aritméticas no processamento de imagens são pontuais (feitas pixel a pixel) e exigem que as imagens de entrada possuam o mesmo tamanho.

**Adição de Imagens** ($s(x,y) = f(x,y) + g(x,y)$):
Finalidade: Realçar similaridades entre imagens.
Redução de Ruído: Ao calcular a média aritmética de $n$ imagens do mesmo cenário, o ruído eletrônico aleatório tende a ser eliminado.Combinação e Fusão: É utilizada para unir resultados de diferentes etapas de processamento ou revelar fenômenos com respostas espectrais distintas.
Escalamento: Como a soma direta pode ultrapassar o valor máximo de intensidade (ex.: 255 em imagens de 8 bits), costuma-se calcular a média dos valores.

**Subtração de Imagens** ($d(x,y) = f(x,y) - g(x,y)$):
Finalidade: Realçar diferenças entre duas imagens.
Detecção de Mudanças: Regiões resultantes em preto (valor $0$) indicam que não houve alteração entre os frames.
Aplicações Médicas: Usada na angiografia por subtração digital, na qual subtrai-se uma imagem "máscara" (sem contraste) de uma imagem "ativa" (com contraste) para destacar os vasos sanguíneos. 

## Operação Geométrica
Transformações GeométricasAs transformações geométricas alteram a posição espacial dos pixels, mapeando as coordenadas da imagem original $(x_0, y_0)$ para novas posições $(x_d, y_d)$ na imagem resultante. Elas são modeladas por transformações afins (via matrizes) e frequentemente necessitam de interpolação para definir a intensidade dos novos pixels68.

Formas de Mapeamento:
Direto: Mapeia da imagem de entrada para a de saída, podendo gerar posições sem pixels atribuídos ou com sobreposições8.
Inverso: Varre a imagem de saída aplicando a matriz inversa ($T^{-1}$) e utiliza interpolação dos vizinhos mais próximos para determinar a intensidade.
Principais Operações Geométricas:
Translação: Move a imagem espacialmente nos eixos $x$ e $y$.
Escala (Ampliação e Redução): Altera as dimensões da imagem.Rotação: Gira a imagem em torno de um ponto segundo um ângulo $\theta$.
Espelhamento / Reflexão (Flip): Inverte a imagem na horizontal ou na vertical.
Cisalhamento (Shear): Deforma a estrutura da imagem nas direções horizontal ou verticaL.
