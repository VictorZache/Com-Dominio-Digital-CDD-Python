'''Faça uma função que receba 2 argumentos e
adicione cada um numa lista diferente. PRODUTO e
PREÇO.
o sistema deve pedir os dados e após isso verificar
se o usuário ainda pretende inserir mais produtos.
Quando terminar de inserir, imprimir as listas'''


def loja(produto,preco):
    produtos=[]
    precos=[]
    for x in range(2):
        produtos.append(produto)
    for z in range(2):
        precos.append(preco)
    return produtos,precos