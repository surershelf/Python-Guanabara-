sp=0
cont=0
for c in range(1,7):
    a = int(input('digite o {}º valor: '.format(c)))
    if a%2==0:
        sp += a
        cont+=1
print('a soma dos {} numeros pares sao {}'.format(cont,sp))


