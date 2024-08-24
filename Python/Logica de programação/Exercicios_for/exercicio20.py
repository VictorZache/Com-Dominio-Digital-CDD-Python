x=0
y=0
'''Receber 10 numeros'''
for l in range(3):
    n=int(input("Digite o numero:"))
    if n>=10 and n<=20:
        x=x+1
    else:
        y=y+1
print(f'{x} numeros entre 10 e 20.{y} Numeros não estão entre 10 e 20')
