'''faça um função que recebe
um número como parâmetro
e verifique se este número é primo'''

n=int(input("Digite o numero:"))

def test_primo(n):
    if (n==1):
        return n,"Não é Primo"
    elif (n==2):
        return n,"É Primo";
    else:
        for x in range(2,n):
            if(n % x==0):
                return n,"Não é Primo"
        return n,"É Primo"

print(test_primo(n))