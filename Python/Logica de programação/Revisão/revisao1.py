#faça um algoritma que receba 2 notase calcule a media aritmetica.
#parte 2: utilize o "for" para pedir as notas
#parte 3: verifique se a nota é valida

soma=0

for x in range(2):
        n1=float(input(f"Digite {x+1} a nota:"))
        while n1 < 0 or n1 >10:
            n1 = float(input(f"Erro, a {x+1} nota é invalida tente novamente:"))
        soma = soma + n1

media=soma/2
print(media)

