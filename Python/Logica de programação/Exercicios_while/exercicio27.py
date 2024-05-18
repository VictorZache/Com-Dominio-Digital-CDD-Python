senha=input("Digite a senha:")
senhaV="123"
control=0
while senha!=senhaV and control <2:
    senha = input("senha incorreta, tente novamente:")
    control+=1
if control== 2 and senha!=senhaV:
    print("Conta bloqueada")
else:
    print("Conta libarada.")

