p=int(input('digite o primeiro termo: '))
r=int(input('digite a razao: '))
termo=p
cont=1
total=0
mais=10
while mais!=0:
    total+=mais
    while cont!=total:
        print('{} -> '.format(termo),end='')
        termo+=r
        cont+=1
    print('pausa')
    mais=int(input('quer ver quantos termos a mais: '))
print('PA finalizada vc viu um total de {} termos'.format(total))
