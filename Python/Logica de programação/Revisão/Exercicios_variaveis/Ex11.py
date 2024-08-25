"""11. Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias.
"""

#Variaveis que recebem os dados
anos = int(input("Digite quantos anos voce tem: "))
meses = int(input("Digite quantos meses: "))
dias = int(input("Digite quantos dias: "))

#Variavel responsavel pelo calculo
diasVivo = (anos*365)+(meses*30)+dias

print(f"Voce esta a {diasVivo} dias vivo!")