'''Faça um programa para imprimir:
1
2 2
3 3 3

.....
n n n n n n ... n'''


num=int(input("Digite o numero fazer a piramide:"))
def piramide(num):
    for x in range(1,num+1):
        for i in range(1,x+1):
            print(x, end=" ")
        print()

piramide(num)

num2=int(input("Digite o numero 2 para fazer a sequencia:"))
def piramide2(num2):
    for x in range(1,num2+1):
        for i in range(1,x+1):
            print(x, end=" ")


piramide2(num2)