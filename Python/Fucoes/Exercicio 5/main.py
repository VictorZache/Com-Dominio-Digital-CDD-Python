from Exercicio5 import *


while True:
    op=int(input("Qual opcao"))

    if op==1:
        produto=input("Qual o produto:")
        preco=int(input("Digite o Preco:"))
        resultado = loja(produto, preco)

    elif op==2:
        print(resultado)
        break


