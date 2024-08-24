"""15. Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente"""

#Variaveis responssaveis por receber os numeros.
n1 = int(input("Digite o Primeiro numero: "))
n2 = int(input("Digite o Segundo numero: "))

#Laço de repetição para garantir que os numeros não sejam iguais,
while n1==n2:
    print("Os numeros não podem ser iguais, tente novamentente.")
    n1 = int(input("Digite o Primeiro numero: "))
    n2 = int(input("Digite o Segundo numero: "))

#Verifica qual numero é maior para criar a ordem crescente.
if n1>n2:
    print(f"Ordem crescente: {n2} - {n1}")
else:
    print(f"Ordem crescente: {n1} - {n2}")

