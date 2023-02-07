from math import factorial
a = int(input('digite um numero para saber o fatorial: '))
b = factorial(a)
print(b)
# ou
c = int(input('digite um numero para saber o fatorial: '))
d = c
f=1
print('Calculando {}!'.format(c))
while d > 0:
    print('{}'.format(d), end='')
    print(' x ' if d > 1 else ' = ', end='')
    f *= d
    d -= 1
print('{}'.format(f))
