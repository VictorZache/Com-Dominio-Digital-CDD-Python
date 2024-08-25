"""4. Crie um algoritmo que receba 3
números e informe qual o maior entre
eles"""

#Variaveis responsaveis por receber os numeros
num1=int(input("Digite o Primeiro numero: "))
num2=int(input("Digite o Segundo numero: "))
num3=int(input("Digite o Terceiro numero: "))

#Verificadores dentro de verificadores, para descobrir qual o maior numero
if num1>num2:
    if num1>num3:
        print(f"O numero {num1} e o maior entre os 3.")
    else:
        print(f"O numero {num3} e o maior entre os 3.")
else:
    if num2>num3:
        print(f"O numero {num2} e o maior entre os 3.")
    else:
        print(f"O numero {num3} e o maior entre os 3.")