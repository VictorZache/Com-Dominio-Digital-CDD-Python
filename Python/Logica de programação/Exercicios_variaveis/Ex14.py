"""14. Escreva um algoritmo para ler uma
temperatura em graus Fahrenheit, calcular
e escrever o valor correspondente em graus
Celsius (baseado na fórmula abaixo):
C = ((F - 32)/9)*5
Observação: Para testar se a sua resposta
está correta saiba que 100 ⍛C = 212 F"""


#Variavel responsavel por receber a temperatura em Fahrenheit
temperaturaF = int(input("Digite a temperatura Fahrenheit: "))

#Variavel responsavel por convewrter a temperatura para Celsius
temperaturaC = int((temperaturaF - 32)/9)*5

print(f"{temperaturaF}° graus Fahrenheit é equivalente a {temperaturaC}° Celsius")