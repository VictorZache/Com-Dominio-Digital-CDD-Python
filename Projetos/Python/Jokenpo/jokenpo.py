import random

class Jokenpo():
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2 = player2
        self.opcoes = ["pedra", "papel", "tesolra"]

    def jokenpo(self):
        if self.player1==self.player2:
            print("Empate")
        elif self.player1 == "pedra" and self.player2== "tesolra":
            print("Jogador 1 venceu")
        elif self.player1 == "tesolra" and self.player2== "papel":
            print("Jogador 1 venceu")
        elif self.player1 == "papel" and self.player2== "pedra":
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")

class JokenpoMaquina(Jokenpo):
    def __init__(self,player1):
        super().__init__(player1,"")
        self.player2=random.choice(self.opcoes)

    def jokenpo(self):
        super().jokenpo()
