class Pessoa:
    def __init__(self,nomePessoa,idadePessoa,pesoPessoa):
        self.nome = nomePessoa
        self.idade = idadePessoa
        self.peso = pesoPessoa

    def comer(self,comida,bebida):
        print(f'{self.nome} Foi comer {comida} com {bebida}')


    def falar(self):
        print(f'{self.nome} esta falando.')

    def dormir(self):
        print(f'{self.nome} dormindo.')

