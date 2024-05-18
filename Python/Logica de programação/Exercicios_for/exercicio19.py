negativos = 0
for l in range(10):
    numero = int(input("digite um numero:"))
    if numero < 0:
        negativos = negativos + 1
print(f'{negativos} numeros são negativos')
