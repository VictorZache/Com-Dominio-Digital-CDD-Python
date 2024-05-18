#crie um algoritmo que leia um numero e diga se ele é par ou impar

rep="S"
while rep=="S" or rep=="s":
    n1=int(input("Digite um numero maior que 0:"))
    div= n1%2
    if div == 0:
        print(f"O numero {n1} é par.")
    else:
        print(f"O numero {n1} é impar.")
    rep=input("Gostaria de testar outro numero?")
print("Programa finalizado")