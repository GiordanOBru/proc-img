# PROCESSAMENTO DE IMAGEM

## Ampliação e Redução

Nessa primeira etapa, a imagem será organizada utilizando diferentes métodos de ampliação e redução: **vizinho mais próximo, interpolação bilinear e interpolação bicúbica**.

**Vizinho mais próximo:** pega o valor do pixel mais próximo e replica esse valor para preencher os novos pixels. É um método simples e rápido, mas pode deixar a imagem mais pixelada.

**Interpolação bilinear:** considera os pixels vizinhos e calcula o novo valor a partir deles, utilizando uma média ponderada. Na ampliação, utiliza os pixels mais próximos para gerar valores intermediários, deixando a imagem mais suave.

**Interpolação bicúbica:** considera uma quantidade maior de pixels vizinhos para calcular o novo valor, proporcionando uma imagem mais suave e com melhor qualidade. É mais complexa e exige mais processamento que os métodos anteriores.
