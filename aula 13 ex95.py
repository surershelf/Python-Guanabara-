totgol=0
time=list()
jog={'nome': '','gols':'','total':''}
golp=list()
while True:
    jog.clear()
    golp.clear()
    totgol=0
    golp.clear()
    jog['nome']=str(input('Nome do Jogador: ')).capitalize()
    a=int(input('Total de partidas jogadas: '))
    for p in range(a):
        golp.append(int(input(f'Quantos gols ele fez na partida {1+p}: ')))
    jog['gols']=golp.copy()
    for gol in jog['gols']:
        totgol+=gol
    jog['total']=totgol
    time.append(jog.copy())
    b=str(input('Quer continuar? [S/N] '))
    while True:
        if b in 'SsNn':
            break
        else:
            b=str(input('Responda apenas com S ou N: '))
    if b in 'Nn':
        break

print(time)
print('-'*40)
print('cod  ',end='')
for i in jog.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15} ',end='')
    print()
print('-'*40)
while True:
    busca=int(input('Digite o código do jogador que quer procurar (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}:')
        for i,g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<< FINALIZANDO >>>')