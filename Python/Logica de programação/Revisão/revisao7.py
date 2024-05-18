'''Parte1:Faça um codigo que recebe o valor da base e da altura do triangulo e calcule sua area. usanddo a formula
A=(base x altura)/2

Parte2 calcaular a area de um quadrado
areaQuadrado= lado*lado ou lado**2

Parte3 perguntar qual calculo o usuario quer fazer'''

escolha=0
while escolha != 3:
    escolha=int(input("Qual calculo você quer fazer? 1 para Triangulo, 2 para quadrado e 3 para terminar o codigo:"))
    if escolha==1:
        base = float(input("Digite o valor da base:"))
        altura = float(input("Digite o valor da altura:"))
        areaT=(base*altura)/2
        print(f' A area do triangulo é igual a {areaT}')
    elif escolha==2:
        lado=float(input("Digite o valor do lado do quadrado:"))
        areaQuadrado=lado*lado
        print(f'A area do quadrado é igual a {areaQuadrado}')
    elif escolha==3:
        print("Programa finalizado.")
    else:
        print("Opção invalida.")