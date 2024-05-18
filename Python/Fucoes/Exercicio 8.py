'''faça um função que recebe uma lista
como argumento e crie uma nova
lista, somente com números únicos.

exemplo:

a[1,2,2,3,4,4,5,3,6,7,6,8]
nova_lista[1,2,3,4,5,6,7,8]'''


a = [1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8]

def separador(a):
    nova_lista= []
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

separador(a)
