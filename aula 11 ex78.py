a=[ ]
mai=men=0
for c in range(0,5):
    a.append(int(input(f'Digite o valor de numero {c}: ')))
    if c==0:
        mai=men=a[c]
    else:
        if a[c]> mai:
            mai = a[c]
        if a[c]<men:
            men = a[c]
print('-'*30)
print (f'Voce digitou os numeros {a}')
print(f'O maior valor digitado foi {mai} nas posições ',end=' ')
for i,v in enumerate(a):
    if v == mai:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {men} nas posições ',end=' ')
for i,v in enumerate(a):
    if v == men:
        print(f'{i}...',end=' ')
print()

