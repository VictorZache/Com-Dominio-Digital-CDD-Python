t1 = input("Qual o primeiro time?")
g1 = int(input("Quantos gols o primiro time fez?"))
t2 = input("Qual o segundo time?")
g2 = int(input("Quantos gols o segundo time fez?"))

if g1==g2:
    print("Empate")
else:
    if g1>g2:
        print(f"O {t1} venceu")
    
    else:
        print(f"O {t2} venceu")



