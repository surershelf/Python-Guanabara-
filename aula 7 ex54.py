from datetime import date

ano= date.today().year
for c in range(1,8):
    a=int(input('digite o ano de nascimento da pessoa numero {} :'.format(c)))
    b=ano-a
    if b<18:
        print('a pessoa numero {} tem {} anos e nao eh de maior'.format(a,b))
        print('\033[34m-=\033[m'*27)
    else:
        print('a pessoa numero {} tem {} anos e eh de maior'.format(c,b))
        print('\033[34m-=\033[m' * 27)
