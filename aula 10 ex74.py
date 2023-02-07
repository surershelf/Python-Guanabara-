from random import randint
maior=menor=0
numeros=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('os numeros sorteados foram:')
for n in numeros:
    print(f'{n}',end=' ')
print(f'\no maior numero eh {max(numeros)}, e o menor eh {min(numeros)}')