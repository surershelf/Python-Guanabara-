list=[]
a=int(input('Digite um valor: '))
list.append(a)
while True:
    b= str(input('Quer continuar? [S/N] '))
    if b in 'Ss':
        a=int(input('Digite outro valor: '))
        list.append(a)
    if b in 'Nn':
        break
print(f'Você digitou {len(list)} valores à sua lista')
print(f'Os valores em ordem decrescente são {list.sort(reverse=True)}')
if 5 in list:
    print(f'O valor de número 5 se encontra na lista, na posição {list.index(5)}')
else:
    print(f'O valor de número 5 não se encontra na lista')
