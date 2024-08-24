'''Perguntar quantos alunos tem na sala e criar um array, unidimensional(vetor)
com o nome de todos os alunos da sala'''



#Criar uma lista vazia
lis_alu = ['','','','','']

#criar um laço de rapetição, usando a lista: o len serve para
for x in range(len(lis_alu)):

    #avancar a quantidade de espaços de acordo com a possiçao de x
    lis_alu[x]=input("Digite o nome dos alunos: ")

#segundo laço de repetição, para mostrar o conteudo da lista em ordem
for y in lis_alu:
    print(y)
