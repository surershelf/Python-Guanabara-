print('=-'*20)
print('10 Termos de uma PA')
print('=-'*20)
p=int(input('Primeiro Termo: '))
r=int(input('Razao da PA: '))
termo=p
cont=1
total=0
mais=10
while mais!=0:
    total+=mais
    while cont <=total:
        print('{} -> '.format(termo),end='')
        termo+=r
        cont+=1
    print('pausa')
    mais=int(input('\ndigite mais quantos termos vc qr  ver a mais:'))
print('fim no total foram {} termos'.format(total))



