
n = int(input('Digite um valor para somar (999 para parar): '))
n1=n
cont=1
while n != 999:
    n=int(input('Digite mais um valor para somar (999 para parar): '))
    n1+=n
    cont+=1
    if n ==999:
        cont-=1
        n1-=999
print('Voce digitou {} numeros e a soma deles eh de {}'.format(cont,n1))

