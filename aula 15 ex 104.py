def leiaint(n):
    while True:
        print('-'*30)
        c = str(input(n))
        if c.isnumeric():
            c=int(c)
            return c
        else:
            print('\033[31mSÃO VÁLIDOS APENAS NÚMEROS\033[m')






n=leiaint('Digite um numero: ')
print(f'O número que você digitou foi {n}')