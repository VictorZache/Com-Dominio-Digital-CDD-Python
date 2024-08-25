"""Faça um programa para ler o nome de uma
pessoa, a sua idade e o seu salário e mostre
essas informações na tela.
"""
#Variavel que recebe uma string nome
nome = input("Digite o seu nome: ")
#Variavel que recebe um inteiro idade
idade = int(input("Digite a sua idade: "))
#Variavel que recebe um float salario
salario = float(input("Digite seu salario: "))

print(f"O seu nome é {nome}\n"
      f"A sua idade é {idade}\n"
      f"O seu salario é R${salario}\n")