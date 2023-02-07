import random

lista = [1, 2, 3, 4, 5]
n1 = random.choice(lista)
escolha = int(input('tente advinhar o numero:'))
if n1 == escolha:
    print('CARALHO VC EH PICA MENO')
else:
    print('VC ERROU TROXA BABACA LIXO LOW ELO IMUNDO MONKEY D. LUFFY')
    print('este era o numero certo {}'.format(n1))
# =======================================================================================================================
velocidade = (float(input('qual a sua velocidade:')))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('voce excedeu o limite maximo da via e sua multa sera de:R${:.2f}'.format(multa))
print('tenha uma otima viajem!!!')
# =======================================================================================================================
num = int(input('digite um numero qualquer: '))
resultado = num % 2
if resultado == 0:
    print('o numero {} eh par'.format(num))
else:
    print('o numero {} eh impar'.format(num))
# =======================================================================================================================
km = float(input('quantos km tem sua viajem: '))
if km <= 200:
    p1 = (km * 0.50)
    print('sua viajem ira custar R${:.2f}'.format(p1))
else:
    p2 = km * 0.45
    print('sua viajem ira custar R${:.2f}'.format(p2))
print('tenha uma otima viajem')
# =======================================================================================================================
ano = int(input('este ano eh bissexto?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} eh bissexto'.format(ano))
else:
    ('o ano {} nao eh bissexto'.format(ano))
# =======================================================================================================================
a = int(input('digite um valor'))
b = int(input('digite um valor'))
c = int(input('digite um valor'))
menor = a
if b < a and c < b:
    menor = b
if c < a and c < b:
    menor = c
print('o menor numero eh {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('maior numero eh {}'.format(maior))
#=======================================================================================================================
salario=(float(input('qual seu salario?')))
if salario >= 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print('o seu aumento eh de {}'.format(novo))
#=======================================================================================================================

