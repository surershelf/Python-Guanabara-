list=[]
par=[]
impar=[]
a=int(input('Digite um valor: '))
list.append(a)
while True:
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)
    b=str(input('Quer continuar? [S/N] '))
    if b in 'Ss':
        a=int(input('Digite outro valor: '))
        list.append(a)
    elif b in 'Nn':
        break
print('=-'*30)
print(f'Os valores da lista são: {list}')
print(f'Os valores pares são: {par}')
print(f'Os valores ímpar são: {impar}')
