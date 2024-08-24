'''Escreva um codigo que permita a leitura das notas de um turma de 5 alunos e guarde num vetor,
calcular a media da turma e contar quantos alunos obtiveram a noma acima desta media
calculanda Escrever a media da turma e o resultado da contagem'''


#Escreva um codigo que permita a leitura das notas de um turma de 5 alunos e guarde num vetor,
nota=["","","","",""]

soma=0
cont=0

for x in range(len(nota)):
    nota[x]=float(input("Digite a nota"))

#somar as notas
for y in range(len(nota)):
    soma+=nota[y]

#contar quantos alunos obtiveram a noma acima desta media
media=soma/5
for z in range(len(nota)):
    if nota[z]>=media:
        cont+=+1



print(f'A media da turma é:  {media}')
print(f'{cont} Alunos estão acima da media.')




