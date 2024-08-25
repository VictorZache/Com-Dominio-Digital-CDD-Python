"""18.Escreva um algoritmo que dado um
arrays, retorno um novo array, com os
elementos em ordem invertida.
entrada:
a=[2,5,4,2,8,5,2]
saída
b=[2,5,8,2,4,5,2]"""

#Lista inicial com 7 valores
listaEntrada = [2,5,4,2,8,5,2]

#Lista de saida que vai receber os valores da lista de entrada
listaSaida = []

#Laço de repetição For que percorre a lista de entrada de tras pra frente (Começa na posição 6, termina na -1, subtraindo 1)
for x in range(6,-1,-1):
    #O comando appende serve para adicionar algo a uma lista, no caso o item que esta na posição x da listaEntrada
    listaSaida.append(listaEntrada[x])

#Mostrar a Lista de siada
print(f"A ordem invertida da Lista de entrada é: {listaSaida}")

