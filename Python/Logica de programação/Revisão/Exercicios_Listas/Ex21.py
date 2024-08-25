"""21. Dado o seguinte array [10, 12, 20, 30, 25,
40, 32, 31, 35, 50, 60] . Crie um novo array
com os dados que estão entre os índices 3 e
8."""

#Lista com os valores e lista que ira receber os valores.
lista = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
novaLista = []

#Laço de repetição pra pegar os numeros na posição desejada da lista e adicionar na nova lista.
for x in range(0,11,1):
    if x>=3 and x<=8:
        novaLista.append(lista[x])

print(f"Lista predefida: {lista}\n"
      f"Lista com os valores das posições de 3 a 8 da primeira lista: {novaLista}")