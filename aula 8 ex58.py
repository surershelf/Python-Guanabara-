import random
from random import randint
print('\033[34m='*45)
print('\033[32m{:=^45}'.format(' JOGO DE ADVINHAÇÃO '))
print('\033[34m=\033[m'*45)
tentativas=1
maquina=random.randint(1,10)
a=int(input('\033[mTente acertar o numero: '))
while a!=maquina:
    a=int(input('Vc errou tente novamente: '))
    tentativas+=1
if tentativas==1:
    print('\033[32mVc acertou de primeira parabens')
elif tentativas <= 3:
    print('\033[33mVc acertou em {} tentativas,foi bem'.format(tentativas))
elif tentativas<=7:
    print('\033[35mMelhore!!! Vc acertou em {} tentativas'.format(tentativas))
else:
    print('\033[31mMELHORE URGENTEMENTE!!! vc acertou em {} tentativas'.format(tentativas))
print('\033[mfim')
