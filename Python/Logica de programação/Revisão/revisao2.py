#Crie um codigo que leia um numero diferente de zero e diga se este numero é positivo ou negativo.
#parte 2: pergunte se o usuario vai querer repetir

rep="S"
while rep=="S" or rep=="s":
    n1=int(input("Digite um numero:"))

    if n1 > 0:
        print(f"O numero {n1} é positivo.")
    else:
        print(f"O numero {n1} é negativo.")
    rep=input("Gostaria de testar outro numero?")
print("Programa finalizado")
