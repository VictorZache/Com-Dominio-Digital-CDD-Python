#Escreva um algoritmo para ler o numero total de eleitores de um municipio, o numero de votos brancos, nulos e validos.
#Calcular e escrever o percentual que cada um representa em relaçao ao total de eleitores.

totalDeEleitores=int(input("Quantos votos tiveram na eleição?"))
validos=int(input("Quantos votos foram validos na eleição?"))
brancos=int(input("Quantos desses votos foram brancos?"))
nulos=int(input("Quantos desses votos foram nulos"))

pBran=(brancos/totalDeEleitores)*100
pNul=(nulos/totalDeEleitores)*100
pVali=(validos/totalDeEleitores)*100

print(f'Porcentagem de Brancos {pBran}%')
print(f'Porcentagem de Nulos {pNul}%')
print(f'Porcentagem de Validos {pVali}%')

