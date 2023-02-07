list = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    not1 = float(input('Primeira nota: '))
    not2 = float(input('Segunda nota: '))
    media = (not1 + not2) / 2
    list.append([nome, [not1, not2], media])
    p = str(input('Quer continuar? [S/N] '))
    if p in 'Nn':
        break
print('=-' * 50)
print(f'{"No.":<5}', end='')
print(f'{"Nome":<20}{"Média"}')
print('\033[1m-\033[m' * 40)
for n, p in enumerate(list):
    print(f'{n:<5}', end='')
    print(f'{p[0].capitalize():<20}{p[2]}')
print('\033[1m-\033[m' * 40)
while True:
    c = int(input('Quer saber a nota de qual aluno? para parar [999]: '))
    if c != 999:
        print(f'As notas do aluno {list[c][0]} são {list[c][1]}')
        print('\033[1m-\033[m' * 40)
    elif c == 999:
        print('Finalizando...')
        break
print('<<< FIM DO PROGRAMA >>>')
