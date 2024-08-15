"""6. Ler um valor e escrever a mensagem É MAIOR
QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10"""

valor = int(input("Digite um numero para saber se ele e maior que 10: "))

#Verificador do valor
if valor>10:
    print(f"O numero {valor} É MAIOR QUE 10!")
else:
    print(f"O numero {valor} NÃO É MAIOR QUE 10!")