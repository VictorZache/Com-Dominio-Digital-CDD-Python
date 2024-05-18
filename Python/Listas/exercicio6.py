'''Alterar o sistema anterior e faça um sistema de login, pedindo a senha do usuario e mostrando seu nome e a
mensagem, login efetuado com sucesso.'''

nomes=["a","b","c","d","e"]
senhas=["1","2","3","4","5"]


cont=int(input("Digite 1 para cadastrar ou dois para fazer login."))

while cont >=1 or cont<=2:
    if cont == 1:
        for i in range(len(nomes)):
            nomes[i] = input(f'Digite o {i + 1}º nome:')
            senhas[i] = input(f'Digite a {i + 1}º senha:')

        for x in range(5):
            print(x + 1, nomes[x], senhas[x])
        cont = int(input("Digite 1 para cadastrar ou dois para fazer login."))

    else:
        nome = input("Digite seu nome usuario:")
        senha=input("Digite sua senha:")

        for i in range(len(nomes)):
            if nome==nomes[i]:
                login=nomes[i]
            else:
                print("Login invalido")





