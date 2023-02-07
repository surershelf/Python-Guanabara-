a=[]
a.append(int(input('Digite um valor: ')))
while True:
    b =str(input('Quer continuar? [S/N] '))
    if b in 'Ss':
        c=(int(input('Digite outro Valor: ')))
        if c not in a:
            a.append(c)
            print('Valor Adcionado!')
        else:
            print('Valor Duplicado! Não irei adicionar...')
    if b in 'Nn':
         break
a.sort()
print(f'Você digitou os números {a}')