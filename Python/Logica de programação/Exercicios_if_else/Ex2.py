"""2. Crie um código que leia um número
diferente de zero e diga se este número
é positivo ou negativo
"""
#Variavel que recebe o numero
numero = int(input("Digite um numero diferente de 0: "))

#Verificador, responsavel por dizer se o numero e positivo ou negativo
if numero>=0:
    print(f"O numero {numero} e positivo.")
else:
    print(f"O numero {numero} e negarivo.")