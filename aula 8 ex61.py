print('=-'*20)
print('10 Termos de uma PA')
print('=-'*20)
p=int(input('Primeiro Termo: '))
r=int(input('Razao da PA: '))
termo=p
cont=1
while cont <=10:
    print('{} -> '.format(termo),end='')
    termo+=r
    cont+=1
print('fim')