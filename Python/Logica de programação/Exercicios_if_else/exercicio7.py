n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))

m = (n1 + n2 + n3)/3
print ("Sua media é: ",m)

if m<4:
    print("Reprovado")
else:
    if m>=7:
        print("Aprovado")
    else:
        print("Recuperação")
