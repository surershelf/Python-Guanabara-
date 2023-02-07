print('-=' * 20)
print('analisador de triangulo')
print('-=' * 20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode se formar um triangulo', end='')
    if r1 == r2 == r3:
        print(' EQUILATERO')
    elif r1 != r2 != r3 and r1 != r3:
        print(' ESCALENO')
    else:
        print(' ISOCELES')
else:
    print('nao podem formar um triangulo')
