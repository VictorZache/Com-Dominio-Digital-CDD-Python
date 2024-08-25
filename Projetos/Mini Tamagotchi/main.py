from classes import *

#Pessoa criada utilizando a Classe Pessoa
p1=Pessoa("Victor",22,"54kg",)

#Manual de comandos
print(f'                     SIMULADOR\n Digite o numero para selecionar a opcao correspondente.\n')
print(f'1-Comer\n2-Parar de Comer \n3-Falar \n4-Parar de Falar \n5-Dormir \n'
      f'6-Parar de Dormir \n7-Matar\n')

#Sistem de selecao
while True:
    opcao = int(input(f"Qual das opcoes de acao {p1.nome} vai tomar? \n"))
    if opcao == 1:
        p1.comer()

    elif opcao == 2:
        p1.comerParar()

    elif opcao==3:
        p1.falar()

    elif opcao == 4:
        p1.falarParar()

    elif opcao == 5:
        p1.dormir()

    elif opcao == 6:
        p1.dormirParar()

    elif opcao == 7:
        p1.morte()
        break

    else:
        print("Comando invalido, tente novamente.\n")