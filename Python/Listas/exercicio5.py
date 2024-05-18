'''Faça um codigo para ler 5 nomes de usuarios e suas respectivas senhas, e armazenar cada lista em um array diferente,
apos completar a digitação, imprimir, nome, senha e posição dos dados no array.'''


nomes=["","","","","",]

senhas=[0,0,0,0,0]

for i in range(len(nomes)):
    nomes[i]=input(f'Digite o {i+1}º nome:')
    senhas[i]=int(input(f'Digite a {i+1}º senha:'))

for x in range(5):
    print(x+1,nomes[x],senhas[x],"\n")


