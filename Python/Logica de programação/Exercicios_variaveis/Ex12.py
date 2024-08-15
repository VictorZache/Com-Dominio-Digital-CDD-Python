"""12. Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores.
"""
#Variaveis que recebem os valors
numEleitores = int(input("Digite o numero total de eleitores: "))
votosBranco = int(input("Digite o numero de Votos em Brancos: "))
votosNulos = int(input("Digite o numero Votos em Nulos: "))
votosValidos = int(input("Digite o numero Votos Validos: "))

#Variaveis que fazem os calculos
percentualBranco = (votosBranco/numEleitores)*100
percentualNulo = (votosNulos/numEleitores)*100
percentualValido = (votosValidos/numEleitores)*100

#Print formatado que so vai mostra duas casas depois do .
print(f"Percentual de votos brancos: {percentualBranco:.2f}%")
print(f"Percentual de votos nulos: {percentualNulo:.2f}%")
print(f"Percentual de votos válidos: {percentualValido:.2f}%")
