from jokenpo import *

while True:
    opcao=int(input("Escolha qual mode de jogo.\n 1-Para 2 jogadores.\n 2-Para jogar contra a maquina.\n"))
    if opcao==1:
        p1 = input("op").lower()
        p2 = input("op").lower()
        partida = Jokenpo(p1,p2)
        partida.jokenpo()
    elif opcao==2:
        p1 = input("op").lower()
        partida = JokenpoMaquina(p1)
        partida.jokenpo()
    else:
        print("Opcao invalida")
        break

