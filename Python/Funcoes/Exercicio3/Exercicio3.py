'''Crie uma função que recebe o nome de
um produto, a quantidade que tem no
estoque e o valor unitário do produto.
Retorne o valor total do meu estoque.'''

    #def estoque(produto, quantidade, valor):
    #valor= quantidade*valor
    #return valor


'''Usando a função estoque que acabamos de criar,
faça um código que cadastre os nomes dos
produtos num array produtos, valor unitário em
um array valor unitário e o retorno da função
estoque no array valortotal.
Depois print os 3 arrays para mostrar que tudo foi
registado.'''


def nome():
    nomeProdutos=[]
    for x in range(3):
        nome=input(f"Digite o nome do produto {x+1}:")
        nomeProdutos.append(nome)
    return nomeProdutos

def valor():
    valorProduto=[]
    for y in range(3):
        valor=float(input(f"Digite o valor do produto {y+1}:"))
        valorProduto.append(valor)
    return valorProduto

def quantidade():
    quantidadeProduto=[]
    for i in range(3):
        quantidade=int(input(f"Digite a quantidade do produto {i+1}:"))
        quantidadeProduto.append(quantidade)
    return quantidadeProduto

def estoque():
    nomeProduto= nome()
    valorProduto = valor()
    quantidadeProduto= quantidade()
    valorEstoque = []

    for z in range(3):
        valorEstoque.append(valorProduto[z]*quantidadeProduto[z])

    return nomeProduto,valorProduto,quantidadeProduto,valorEstoque
