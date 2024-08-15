'''Faça um programa, com uma função que necessite
de um argumento.
A função retorna o valor de caractere ‘P’, se seu
argumento for positivo, e ‘N’, se seu argumento for
negativo e Z se o argumento for zero.'''


num=int(input("Digite um numero:"))

def verificador(num):
    if num==0:
        return "Z"
    elif num>0:
        return "P"
    else:
        return "N"

resposta=verificador(num)

print(resposta)
