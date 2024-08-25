"""16. Escreva um algoritmo para ler a hora de
início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia
seguinte
"""

#Variaveis responsaveis por receber as horas
horaIni = int(input("Digite a hora de Inicio do jogo: "))
horaFim = int(input("Digite a hora do Fim do jogo: "))


#Verifica se as horas do termino da partida sao maiores que as de inicio
if horaFim>horaIni:
    #Se sim, ele faz a subtracao normalmente
    tempoPartida = horaFim - horaIni
else:
    #Se nao, Subtrai 24 horas das horas iniciais e soma com as horas do termino
    tempoPartida = (24 - horaIni) + horaFim

print(tempoPartida)
