'''Faça uma função que possa
receber um número não

determinado de argumentos

e some todos eles.'''


def soma(*args):
    total=0
    for x in args:
        total=total+x
    return total

resultado=soma(1,2,3,4,5,6,7,8,)

print(resultado)



