from random import randint
from time import sleep
aleat=list()


def sorteia(*num):
    print('Sorteando 5 valores: ',end='')
    for c in range(0,5):
        aleat.append(randint(1, 10))
    for v in aleat:
        sleep(0.5)
        print(f'{v} ', end='')
    print('PRONTO')


def somapar(*num):
    soma=0
    for c in aleat:
        if c % 2==0:
            soma+=c
    print(f'A soma dos valores pares são: {soma} ')


sorteia()
somapar(aleat)