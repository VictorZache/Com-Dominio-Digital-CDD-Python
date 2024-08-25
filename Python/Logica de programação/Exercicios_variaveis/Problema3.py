"""Faça um programa para calcular a média de 2 notas e
mostrar essa média e o nome do aluno."""

#Variaveis que recebem os numeros e o nome pelo usuario
nome = input("Digite o nome do aluno")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

#Variavel que realiza o calculo da media
media = (num1+num2)/2

#Mosta o resultado do calculo
print(f"A media do aluno {nome} é {media}")