#Crie um algoritmo que receba 3 numeros e informe qual o maior entre eles
#Agora usado o for para pedir as notas e apensa um if

numeroMaior=0
for x in range(3):
    n1=int(input(("Digite o primeiro numero:")))
    if n1 > numeroMaior:
        numeroMaior = n1
print(numeroMaior)


