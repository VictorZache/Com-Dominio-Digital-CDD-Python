"""Ler 2 números, efetuar as 4 operações
matemáticas e mostrar os resultados.
"""
#Variaveis que recebem os numeros
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

#Variaveis resposaveis por realizar as operações
soma = num1+num2
sub = num1-num2
multi = num1*num2
div = num1/num2

print(f"A soma dos numeros {num1} e {num2} é igual a {soma}\n"
      f"A subtração dos numeros {num1} e {num2} é igual a {sub}\n"
      f"A multiplicação dos numeros {num1} e {num2} é igual a {multi}\n"
      f"A divisão dos numeros {num1} e {num2} é igual a {div}\n")