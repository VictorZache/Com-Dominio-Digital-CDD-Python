"""3. Crie um código que leia a idade de
uma pessoa e diga em qual ano ela
nasceu"""

#Variaveis para receber valores
anoNacimento = int(input("Digite o seu ano de nascimento: "))
anoAtual = int(input("Em que ano estamos?"))
aniversario = input("Voce ja completou aniversario esse ano? s/n ")

#Verificador para saber se o usuario ja fez aniversario
if aniversario=="s"or aniversario =="S":
    anos = (anoAtual - anoNacimento)
    print(f"Voce tem {anos} anos")
else:
    anos = (anoAtual - anoNacimento)-1
    print(f"Voce tem {anos} anos")


