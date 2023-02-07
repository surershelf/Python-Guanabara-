matriz= [[0,0,0],[0,0,0],[0,0,0]]
par=somcol=maival=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para posição [{l},{c}]: '))
        if matriz[l][c] %2==0:
            par+=matriz[l][c]
        somcol+=matriz[l][2]
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print(f'A soma de todos os números pares são: {par}')
print(f'A soma da terceira coluna é: {somcol}')
for c in range(0,3):
    if c ==0:
        maival = matriz[1][c]
    else:
        if maival < matriz[1][c]:
            maival = matriz[1][c]
print(f'O maior valor da segunda linha : {maival}')