a=0
while True:
    a=(int(input('Quer ver a tabuada de qual numero: ')))
    if a<0:
        break
    print('-'*30)
    for c in range(1,11):
        print(a,'x',c,'=',a*c)
    print('-' * 30)
print('FIM')
