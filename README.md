# Desafio - Processamento Digital de Imagens

Script que recebe e customiza a imagem de um produto.


## Pré-requisitos

Bibliotecas [Pillow](https://pillow.readthedocs.io/en/stable/ "Pillow docs") e [NumPy](https://numpy.org/ "Numpy Homepage").

## Como usar

1. Baixe esse repositório
2. Abra um terminal na pasta do repositório
3. Digite no terminal: `python3 gocase.py nome_da_imagem nome_da_fonte texto coordenadas` e aperte enter.

A ordem dos parâmetros é essencial.

O nome das imagens deve ser o mesmo de uma das imagens da pasta *mockups*.

O nome das fontes deve ser o mesmo de uma das fontes da pasta *fonts*.

Se quiser adicionar mais imagens ou fontes, basta adicioná-las nessas pastas.

A imagem customizada será gerada na pasta do repositório com o nome `nome_da_imagem_texto`.

## Exemplos

* Exemplo 1: `python3 gocase.py flamingos mighty-river Tito 180,230`

![alt text](Exemplos/flamingos_Tito.jpg "Exemplo 1")

* Exemplo 2: `python3 gocase.py night-tones be-true-to-your-school 'Claudemir Woche' 170,230` 

![alt text](Exemplos/night-tones_Claudemir_Woche.jpg "Exemplo 2")

* Exemplo 3: `python3 gocase.py mandala superclarendon Gocase 170,255`

![alt text](Exemplos/mandala_Gocase.jpg "Exemplo 3")

## Questões Adicionais

1. A partir de um script de reconhecimento de objetos, obter as coordenadas de onde ficam esses itens na imagem e não permitir que customizações sejam feitas numa região dessas coordenadas.

2. Implementar uma função que receba como parâmetro: imagem a ser customizada, fonte a ser usada e o nome a ser plotado, e retorne o tamanho de fonte ideal. Sendo a implementação da seguinte forma: obter o tamanho do texto com a fonte e com tamanho de fonte 1 e assim ir incrementando o tamanho de fonte até que se atinga um tamanho de texto necessário.O tamanho de texto necessário é a fração da imagem que terá o nome plotado. **Feature Implementada** 

3. Obter dados de imagens geradas pelo script e suas correspondentes capinhas que passaram pelo processo de fabricação. Utilizar esses dados como treinamento de um modelo de rede neural para que ele receba uma imagem gerada pelo script e exiba como saída uma aproximação da imagem real que será gerada pela fábrica. 
