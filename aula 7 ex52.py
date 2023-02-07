num=int(input('digite um numero: '))
tot= 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[32m',end=' ')
        tot+=1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
print('\n \033[mO numero {} foi divisivel {} vezes'.format(num,tot))
if tot>2:
    print('O numero {} nao eh primo.'.format(num))
else:
    print('O numero {} eh primo.'.format(num))