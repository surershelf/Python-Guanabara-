from random import randint
from time import sleep
from operator import itemgetter
print('-'*40)
print(f'{"JOGO DE DADOS":^40}')
print('-'*40)
py={'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4':randint(1,6)}
ranking=dict()
for j,d in py.items():
    print(f'O {j} rolou o dado de número: {d}')
    sleep(1)
print('-'*40)
print(f'{"RANKING":^40}')
print('-'*40)
ranking=sorted(py.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    print(f'{1+i} lugar:{v[0]} com {v[1]}.')
    sleep(1)