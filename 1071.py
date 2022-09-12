maior = 0
menor = 0

X=int(input())
Y=int(input())

menor, maior = sorted([X, Y])
 
soma = 0

for i in range(menor+1,maior):

    if i%2 != 0:
       soma=soma+i
print(soma)
       
