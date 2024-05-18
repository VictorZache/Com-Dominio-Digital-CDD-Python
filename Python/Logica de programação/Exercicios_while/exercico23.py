'''Ler 10 valores e dar a media aritimetica desse 10 numeros. Usando while.'''
n=0
soma=0

while n<10:
    print(f'valor de n é {n}')
    numero= int(input("digite o numero"))
    soma=soma+numero
    n=n+1

media=soma/10
print(media)