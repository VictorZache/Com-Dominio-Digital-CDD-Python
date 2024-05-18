#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas
#em dias. Considere ano com 365 e mes com 30 dias.

idade=int(input("Quantos anos você tem?"))
mes=int(input("Quantos quantos meses desde o seu ultimo aniversario?"))
dia=int(input("E quantos dias ?"))

diasAnos=idade*365
diasMes=mes*30

diasVivo=diasAnos+diasMes+dia

print(f'Você sobrevivel por {diasVivo} dias no Brasil, parabens')