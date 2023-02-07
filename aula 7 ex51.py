
print('=-'*20)
print('10 Termos de uma PA')
print('=-'*20)
a=int(input('Primeiro termo: '))
b=int(input('razao: '))
c=a+(10) * b
for c in range(a,c,b):
    print(c,end='->')
print('acabou')