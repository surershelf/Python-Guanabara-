from random import randint
import time
print('-'*40)
print(f'{"MEGA SENA":^40}')
print('-'*40)
time.sleep(1)
a=int(input('Quantos jogos quer sortear? '))
for c in range(0,a):
    g =[randint(1, 60),randint(1, 60),randint(1, 60),randint(1, 60),randint(1, 60),randint(1, 60)]
    print(f'Jogo {1+c}: {sorted(g)} ')
    time.sleep(1)
print('-'*40)
print(f'{"BOA SORTE":^40}')
print('-'*40)
# MEU JEITO
#JEITO DO GUANABARA
print('-'*40)
print(f'{"MEGA SENA":^40}')
print('-'*40)
list=[]
jogos=[]
quant=int(input('Quantos jogos voce quer que eu sorteie: '))
tot=1
while tot<=quant:
    cont=0
    while True:
        num=randint(1,60)
        if num not in list:
            list.append(num)
            cont+=1
        if cont>=6:
            break
    list.sort()
    jogos.append(list[:])
    list.clear()
    tot+=1
print('sorteando numeros')
for i,l in enumerate(jogos):
    print(f'Jogo {1+i}: {l}')
print('-'*40)
print(f'{"BOA SORTE":^40}')
print('-'*40)

