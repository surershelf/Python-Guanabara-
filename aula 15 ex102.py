def fatorial(n=1,show=False):
    f = 1
    if show==False:
        print('-'*40)
        for c in range(n,0,-1):
            f*=c
        return f
    if show==True:
        print('-'*40)
        for c in range(n,0,-1):
            print(f'{c} ', end='')
            f*=c
            if c>1:
                print('x ',end='')
            else:
                print('= ',end='')
        return f


n=int(input('Quer ver o fatorial de qual número: '))
print(fatorial(n,show=True))