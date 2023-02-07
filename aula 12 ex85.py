num=[[],[]]
for n in range(0,7):
    a=int(input(f'Digite o {1+n}º numero: '))
    if a%2==0:
        num[0].append(a)
    else:
        num[1].append(a)
print(f'Os valores pares da lista são: {sorted(num[0])}')
print(f'Os valores ímpares da lista são: {sorted(num[1])}')