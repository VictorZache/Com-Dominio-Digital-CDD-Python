class Pessoa:                                                          #Classe pessoa, responsavel por criar uma pessoa.
    def __init__(self,nome,idade,peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.atividade=None


    def comer(self):                                                    # Metodo para comecar a comer.
        if self.atividade == None:                                      #Condicao para que a pessoa comece a uma acao.
            self.atividade = "Comer"                                    #Pessoa recebera o status, da acao selecionada.
            print (f'{self.nome} comecou  a {self.atividade}.\n')
        else:                                                           #Caso a condicao nao seja atendida, ou seja, a pessoa ja estaja realizando uma acao.
            print(f'{self.nome} esta a {self.atividade}.\n')

    def comerParar(self):                                               #Metodo para parar uma acao.
        if self.atividade == "Comer":                                   #Condicao para finalizar determinada acao, deve ser correspondente a acao que ele esteja realizando.
            print(f'{self.nome} parou de {self.atividade}.\n')
            self.atividade = None                                       #Pessoa vai ter seu status de acao zerado.
        elif self.atividade == None:
            print(f'{self.nome} nao esta realizando uma acao.\n')       #Caso ele ja esteja com o status zerado.
        else:                                                           #Caso a pessoa esteja realizando uma acao que nao seja correspondete, para poder ser finalizada.
            print(f'{self.nome} nao pode parar de {self.atividade} com essa opcao, tente outro comando.\n')

    def falar(self):                                                    # Metodo para comecar a falar
        if self.atividade == None:
            self.atividade="Falar"
            print (f'{self.nome} comecou a {self.atividade}.\n')
        else:
            print(f'{self.nome} esta a {self.atividade}.\n')

    def falarParar(self):                                                 # Metodo para parar de falar comer
        if self.atividade == "Falar":
            print(f'{self.nome} parou de {self.atividade}.\n')
            self.atividade = None
        elif self.atividade == None:
            print(f'{self.nome} nao esta realizando uma acao.\n')
        else:
            print(f'{self.nome} nao pode parar de {self.atividade} com essa opcao, tente outro comando.\n')

    def dormir(self):                                                       # Metodo para comecar a dormir
        if self.atividade == None:
            self.atividade = "Dormir"
            print(f'{self.nome} comecou a {self.atividade}.\n')
        else:
            print(f'{self.nome} esta a {self.atividade}.\n')

    def dormirParar(self):                                                  # Metodo para parar de dormir
        if self.atividade == "Dormir":
            print(f'{self.nome} parou de {self.atividade}.\n')
            self.atividade = None
        elif self.atividade == None:
            print(f'{self.nome} nao esta realizando uma acao.\n')
        else:
            print(f'{self.nome} nao pode parar de {self.atividade} com essa opcao, tente outro comando.\n')



    def morte(self):                                                        #Metodo para matar a pessoa e terminar a simulacao.
        self.atividade="Morreu"                                             #Este metodo nao leva em conta se a pessoa esta ou nao realizando uma acao
        print(f'{self.nome} esta {self.atividade}.\n')


