#Escreva um algoritmo para ler a hora de inicio e a hora de fim de um jogo de xadrez
#Considere apenas hora inteiras, sem os minutos
#E calcule a duraçao do jogo em horas, sabendo que o tempo
#maximo de duraçao do jogo e de 24 horas e sabendo que o jogo pode iniciar em um dia e terminar no seguinte

horaIn=int(input("Digite a hora de inicio:"))
horaFi=int(input("Digite a Hora de termino:"))


if horaIn<horaFi:
    tempPar=horaFi-horaIn
else:
    tempPar=24 - horaIn + horaFi


print(tempPar)
