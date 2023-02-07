maior = 0
menor = 0
for c in range(1, 6):
    a = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
