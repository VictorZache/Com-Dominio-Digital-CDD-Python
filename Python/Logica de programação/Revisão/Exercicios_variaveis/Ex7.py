"""7. Faça um código que receba o valor da
base e da altura de um triângulo e
calcule sua área. usando a fórmula A =
(base x Altura ) /2"""

#Variaveis que recebem os valores da base e da altura do triângulo
base = int(input("Digite o valor da base do triângulo: "))
altura = int(input("Digite o valor da altura do triângulo: "))

#Variavel que calcula os valores da base e da altura do triângulo
area = (base*altura)/2

print(f"A area do triângulo e: {area}")