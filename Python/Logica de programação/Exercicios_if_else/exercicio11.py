hora1=int(input("Digite a primeira hora:"))
min1=int(input("Digite digite os minutos da primeira hora:"))
hora2=int(input("Digite a Segunda hora:"))
min2=int(input("Digite digite os minutos da segunda hora:"))
if hora1>12:
    hora1 = hora1 - 12

if hora2>12:
    hora2 = hora2 - 12

horaT=hora1+hora2

minutosT= min1+min2

if minutosT >= 60:
    minutosT=minutosT-60
    horaT = horaT +1

print(horaT, ":" ,minutosT)














