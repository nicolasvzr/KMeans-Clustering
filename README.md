
# K-Means Clustering - Machine Learning II  

Este projeto faz parte da disciplina **Machine Learning II** do curso de **Ciência de Dados**.  

O objetivo é implementar o algoritmo **K-Means** para **agrupamento de dados bidimensionais** e determinar o número ideal de clusters usando o **método do cotovelo**.

## Sobre  

O projeto implementa o algoritmo **K-Means**, um método de **aprendizado não supervisionado** usado para **agrupamento de dados**.  
A análise é feita em um conjunto de dados bidimensional, onde o objetivo é identificar padrões e **determinar o número ideal de clusters** usando o **método do cotovelo (Elbow Method)**.


## Bibliotecas Utilizadas  
O projeto utiliza as seguintes bibliotecas Python:  

- `numpy` → Manipulação de arrays e cálculos numéricos  
- `matplotlib` → Visualização de gráficos  
- `scikit-learn` → Implementação do K-Means  


## Etapas do Código  

1. Criar um **conjunto de dados bidimensional**  
2. Testar valores de `K` (1 a 10) e calcular a **inércia**  
3. Gerar um **gráfico do método do cotovelo** para encontrar o melhor `K`  
4. Ajustar `K=2` e **visualizar os clusters**  


## Resultados  

Abaixo está o gráfico gerado pelo método do cotovelo, que ajuda a determinar o número ideal de clusters:  

<img src="https://github.com/user-attachments/assets/1856c98a-63e4-4170-ad46-cc2a0ea42aaf" width="450">

Após determinar `K=2`, o algoritmo agrupa os pontos de dados, destacando os centroides:  

<img src="https://github.com/user-attachments/assets/481043a0-f74f-476b-ac44-b935958fbc22" width="450">


