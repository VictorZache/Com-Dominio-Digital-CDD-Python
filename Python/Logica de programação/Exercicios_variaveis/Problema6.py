"""Duas variáveis (A e B) possuem valores distintos (A=5
e B= 10), Crie um algoritmo que armazene esses
dois valores nessas duas variáveis, e efetue a troca
dos valores de forma que a variável A passe a
possuir o valor da variável B e que a variável B
passe a possuir o valor da variável A. Por fim,
apresentar os valores trocado."""

#Variaveis com os numeros iniciais
varA = 5
varB = 10

print(f"Antes da troca: A = {varA}, B = {varB}")

#Variavel C recebe o valor de A
varC = varA
#Variavel A recebe o valor de B
varA = varB
#Variavel B recebe o valor de C
varB = varC

print(f"Após a troca: A = {varA}, B = {varB}")

