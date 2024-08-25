"""20. Escreva um algoritmo que receba do
usuário 10 números, guarde num array e
mostre:
1. todos os números ímpares;
2. todos os números pares;
3. todos os números positivos;
4. todos os números negativos;
5. todos os zeros que aparecem no array
"""

#Listas e variavel que irão receber os numeros
numArray = []
arrayImp = []
arrayPar = []
arrayPos = []
arrayNeg = []
contZ = 0

#Laço que ira receber os numeros
for x in range(0, 10, 1):
    num = int(input(f"Digite o {x+1}° numero: "))
    numArray.append(num)

print(numArray)

#Laço para percorrer a Lista com todos os numeros, separalos nas listas correspondentes
for y in range(0,10,1):
    if numArray[y]%2==1:
        arrayImp.append(numArray[y])
    else:
        arrayPar.append(numArray[y])

    if numArray[y]>0:
        arrayPos.append(numArray[y])
    elif numArray[y]==0:
        contZ += 1
    else:
        arrayNeg.append(numArray[y])


print(f"Numeros Impares: {arrayImp}\n"
      f"Numeros Pares: {arrayPar}\n"
      f"Numeros Positivos: {arrayPos}\n"
      f"Numeros Negativos: {arrayNeg}\n"
      f"Quantidade de numeros Zero: {contZ}\n")
