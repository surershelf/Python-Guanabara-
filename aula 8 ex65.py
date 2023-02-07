a = int(input('digite um valor: '))
cont = 1
soma = maior = menor = a
b = str(input('Quer continuar [S/N] :'))
while b in 'Ss':
    a = int(input('digite outro valor: '))
    cont += 1
    soma += a
    if a > maior:
        maior = a
    if a < menor:
        menor = a
    b = str(input('quer continuar [S/N] :'))
print('Vc digitou {} numeros e a media deles é {}'.format(cont, soma / cont))
print('O maior numero é {} e o menor número é {} '.format(maior, menor))
