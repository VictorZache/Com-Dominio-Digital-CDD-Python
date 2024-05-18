#crie um codigo que leia a idade de uma pessoa e diga em qual ano ela nasceu
#parte 2: resolva o bug, que ocorrera caso ele não tenha feito aniversario

idade=int(input("Digite sua idade:"))
anoAtual=int(input("Qual o ano atual?"))
aniversario=input(("Você ja fez aniversario esse ano S/N?"))
anoDeNascimento = anoAtual - idade
if aniversario=="S" or aniversario=="s":
    print(f'Seu ano de nascimento é {anoDeNascimento}')
else:
    print(f'Seu ano de nascimento é {anoDeNascimento - 1}')



