
totgol=0
jog={'nome': '','gols':'','total':''}
golp=list()
jog['nome']=str(input('Nome do Jogador: ')).capitalize()
a=int(input('Total de partidas jogadas: '))
for p in range(a):
    golp.append(int(input(f'Quantos gols ele fez na partida {1+p}: ')))
jog['gols']=golp
for gol in jog['gols']:
    totgol+=gol
jog['total']=totgol
print('-='*30)
print(jog)
print('-='*30)
for i,v in jog.items():
    print(f'O {i} tem valor {v}')
print('-='*30)
print(f'O jogador {jog["nome"]} jogou {a} partidas')
for d,g in enumerate(jog["gols"]):
    print(f'=> na partida {1+d} ele fez {g} gols')
print(f'totalizando um total de {jog["total"]} gols')