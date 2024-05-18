a=[0,0,0,0,0,0,0,0,0,0]
m=[0,0,0,0,0,0,0,0,0,0]
b=int(input("Digite o numero:"))

for i in range(len(a)):
    a[i]=int(input("Digite os 10 numero"))

for x in range(len(a)):
    m[x]=a[x]*b
print(a)
print(m)