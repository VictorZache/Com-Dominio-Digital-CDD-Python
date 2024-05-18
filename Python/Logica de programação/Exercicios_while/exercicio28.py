a1=float(input("Digite a primeira nota:"))
while a1<0 or a1>10:
    a1 = float(input("A primeira nota não é valida, tente novamente:"))
a2=float(input("Digite a segunda nota:"))
while a2<0 or a2>10:
    a2 = float(input("A segunda nota não é valida, tente novamente:"))
soma=a1+a2
div=soma/2
print(div)