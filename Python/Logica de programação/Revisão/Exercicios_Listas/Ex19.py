"""19. Usando While escreva um algoritmo
que preencha um array A com os 10
primeiros números ímpares, iniciando por
zero
saída
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""

#Lista vazia que recebera os numeros impares.
arrayA = []

#Variaveis de controle, a variavel cont serve para o while saber quando parar e a num para verificar se o numero é impar.
cont = 0
num = 0

#Laço de repetição while, que vai continuar enquanto a variavel cont for diferente de 10.
while cont!=10:
    #Verifica se a variavel num dividida por 2 tem como mod 1.
    if num%2 == 1:
        #Se sim, arrayA Recebe num, e as variaveis recebem +1
        arrayA.append(num)
        cont += 1
        num += 1
    else:
        #Se não, só a variavel num recebe +1
        num += 1

print(f"Os 10 primeiros numero impares são: {arrayA}")