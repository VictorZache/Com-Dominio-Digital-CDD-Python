alunos=int(input("Digite o numero de alunos:"))
controle=0
soma=0

while alunos > controle:
    nota=float(input("Digite a nota:"))
    soma=soma+nota
    controle= controle+1

media=soma/alunos
print(media)
