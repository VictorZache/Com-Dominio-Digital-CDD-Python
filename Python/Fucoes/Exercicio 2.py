'''Faça uma função que conte quantas
vogais tem num texto.

texto
O rato roeu a roupa do rei de Roma'''


texto="O rato roeu a roupa do rei de Roma!"
vogais="aeiouAEIOU"

def contarvogais(texto):
    cont = 0
    for x in range(len(texto)):
        if texto[x] in vogais:
            cont+=1
    print(cont)

contarvogais(texto)