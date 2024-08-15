'''Faça uma função que receba
um texto como argumento,
mostre a quantidade de
letras e também imprima o

texto ao contrário'''

texto=input("Digite um texto:")

def textoLetras(texto):
    letras=0
    textoContrario=""
    for x in texto:
        letras+=1
    for i in range(len(texto) -1,-1,-1):
        textoContrario+=texto[i]

    return letras, textoContrario

resultado=textoLetras(texto)

print(resultado)