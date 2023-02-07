n = int(input('digite um numero:'))
a = n + 1
s = n - 1
print('analisando o numero {},seu antecessor eh {}, e seu sucessor eh {}'.format(n, a, s))
# =============================================================================================
nu = int(input('outro numero:'))
d = nu * 2
du = nu * 3
r = nu ** (1 / 2)
print('o resultado x2 eh {},o resultado x3 eh {},o resultado da raiz eh {}'.format(d, du, r))
# =============================================================================================
n1 = float(input('primeira nota '))
n2 = float(input('segunda nota '))
media = (n1 + n2) / 2
print('a media entre {} e {} eh {}'.format(n1, n2, media))
# =============================================================================================
medida = float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('convertida em cm eh {}cm e em mm eh {}mm'.format(cm, mm))
# =============================================================================================
real = float(input('quanto vc tem na carteira? R$'))
dolar = real / 5.28
print('com R${:.2f} voce compra U${:.2f}'.format(real, dolar))
# =============================================================================================
larg = float(input('esta eh a largura da parede: '))
alt = float(input('esta eh a altura da parede: '))
area = larg * alt
print('a dimensao da sua parede eh de {} e {}, a area eh de {}m2'.format(larg, alt, area))
tinta = area / 2
print = ('para pintar esta parede eh necessario de {}L de tinta'.format(tinta))
# =============================================================================================
