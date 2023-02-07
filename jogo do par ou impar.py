
from random import randint
n=0
resultado=n%2
contvit=0
print('-'*30)
print('\033[33mJOGO DO PAR OU IMPAR\033[m')
print('-'*30)
while True:
    maq = randint(1, 10)
    a=str(input('Par ou Impar[P/I]: ')).strip().upper()
    n=int(input('Digite um numero : '))
    print(f'A maquina jogou \033[4m{maq}\033[m, e a soma eh \033[4m{n+maq}\033[m, entao ',end='')
    if a in 'Ii':
        resultado=maq+n
        resultado=resultado%2
        if resultado==1:
            print('\033[32mvoce ganhou!\033[m')
            contvit+=1
            print('\033[35mVamos jogar novamente\033[m')
            print('-'*30)
        elif resultado==0:
            print('\033[31mvoce perdeu!\033[m')
            break
    elif a in 'Pp':
        resultado=maq+n
        resultado=resultado%2
        if resultado==0:
            print('\033[32mvoce ganhou!\033[m')
            contvit+=1
            print('\033[35mVamos jogar novamente\033[m')
            print('-'*30)
        elif resultado==1:
            print('\033[31mvoce perdeu!\033[m')
            break
print(f'\033[31mGAME OVER\033[m, e voce ganhou {contvit} vitorias')










