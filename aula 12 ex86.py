mat=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        mat[l][c] = int(input(f'Digite o valor para a posição [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{mat[l] [c]:^5}]',end='')
    print()