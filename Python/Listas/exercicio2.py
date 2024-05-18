'''Escreva um codigo que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, calcular
a media da turma e contar quantos alunos obtiveram nota acima desta media, calular e escrever a media da turma e
o resultado da contaguem.'''

notaTurma=["","","","",""]
soma=0
cont=0

for x in range(len(notaTurma)):
    notaTurma[x]=float(input(f'Digite a nota do {x+1}º aluno:'))

for y in range(len(notaTurma)):
    soma=notaTurma[y]+soma

media=soma/5

for z in range(len(notaTurma)):
    if media >= notaTurma[z]:
        cont+=1


print(f'A soma das notas da turma foi de: {soma}')
print(f'A media da turma é: {media}')
print(f'{cont} Alunos estão na media ou acima da meida.')

