"""17.As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem
compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e
escreva o custo total da compra"""

#Variavel que recebe o quantidade de macas
quantidade = int(input("Quantas maçãs voce vai comprar: "))

#Verificada se a quantidade de macas e maior que 12 para aplicar o deconto
if quantidade>=12:
    total = quantidade*1
    print(f"O valor total das maçãs {quantidade} foi de {total}")
else:
    total = quantidade*1.3
    print(f"O valor total das maçãs {quantidade} foi de {total}")


