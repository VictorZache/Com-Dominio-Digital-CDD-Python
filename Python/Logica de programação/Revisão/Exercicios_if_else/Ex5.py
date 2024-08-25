"""5. Crie um algoritmo que leia um
número e diga se ele é par ou ímpar"""

#Variavel que recebe o valor
num = int(input("Digite um numero para saber se ele e impar ou par: "))

#Verificador do resultado de um calculo
if num%2==0:
    print(f"O numero {num} e PAR!")
else:
    print(f"O numero {num} e IMPAR!")