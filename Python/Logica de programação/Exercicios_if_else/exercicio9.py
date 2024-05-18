litros=float(input("Quantos litros"))

E=4.90
G=5.80

if comb=="G" or comb=="g":
    totalG=litros*G
    print(totalG)
elif comb== "E" or comb=="e":
    totalE = litros*E
    print(totalE)
else:
    print("Combustivel Invalido")