soma=0
divisao=0
for x in range(10):
    n=float(input("Digite a a nota:"))
    if n>=0 and n<=10:
        soma = soma+n
        media = soma / 3
        divisao = divisao + 1
if divisao !=0:
    media = soma/divisao
    print(media)
else:
    print("Ai vc me quebra ne vei.")
