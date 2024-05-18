#criar um array tamanho 5 e preencher com os nomes dos 5 alunos, informado pelo usuario

alunos=["","","","",""]

for x in range(len(alunos)):
    alunos[x]=input("Digite o nome do aluno.")

for y in range(len(alunos)):
    print(y,alunos[y])
