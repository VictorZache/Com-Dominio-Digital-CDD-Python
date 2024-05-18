'''Faça um codigo que leia 5 numeros e armazenar em um vetor. Apos a leitura total dos 5 numeros,
o codigo deve escrever esses numeros lidos na ordem inversa.'''

numeros=[0,0,0,0,0]

for x in range(5):
    numeros[x]=int(input(f'Digete o {x+1}º numero:'))

for i in range(4,-1,-1):
    print(numeros[i])

