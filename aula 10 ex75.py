par=0
num=(int(input('Digite um valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Mais um valor: ')),
     int(input('O último valor: ')))
print(f'Você digitou os valores {num}')
f= num.count(9)
print (f'O número nove apareceu {f} vez')
if 3 in num :
    print (f'O número três apareceu na {1+num.index(3)}ª posição')
else:
    print('Não apreceu nenhum número três')
for n in num:
    if n % 2==0:
        par+=1
print (f'Os números pares que apareceram foram {par}')