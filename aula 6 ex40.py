n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
media = (n1 + n2 + n3) / 3
print('\033[4;35m', media, '\033[m')
if media < 5.0:
    print('\033[31m REPROVADO\033[m')
elif media > 5.0 and media < 6.9:
    print('\033[36m RECUPERA;AO\033[m')
else:
    print('\033[32m APROVADO \033[m')
