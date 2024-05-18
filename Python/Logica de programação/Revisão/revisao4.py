#Crie um algoritmo que receba 3 numeros e informe qual o maior entre eles

n1=int(input(("Digite o primeiro numero:")))
n2=int(input(("Digite o segundo numero:")))
n3=int(input(("Digite o terceiro numero:")))

if n1 > n2 and n1 > n3:
    print(f"O primeiro numero é o maior: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O segundo numero é o maior: {n2}")
else:
    print(f"O terceiro numero é o maior: {n3}")