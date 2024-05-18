#Escreva um algoritmo para ler dois valores(considere que não serão lidos valores iguais) e escrevê-los em ordem crecente

n1=int(input("Digite o primeiro numero:"))
n2=int(input("Digite o segundo numero:"))

if n1 > n2:
    print(n2, n1)
else:
    print(n1,n2)