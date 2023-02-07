list = []
pessoas = []
mai = men = 0
a = str(input('Digite o nome de uma pessoa: '))
b = float(input('Digite o peso da pessoa: '))
while True:
    if b > mai:
        mai = men = b
    else:
        if b > mai:
            mai = b
        elif b < men:
            men = b
    pessoas.append(a)
    pessoas.append(b)
    list.append(pessoas[:])
    pessoas.clear()
    c = str(input('Quer continuar? [S/N] '))
    if c in 'Ss':
        a = str(input('Digite o nome de outra pessoa: '))
        b = float(input('Digite o peso da pessoa: '))
    elif c in 'Nn':
        break
print(f'Foram cadastradas {len(list)} pessoas, as quais são {list}')
print(f'O maior peso registrado é de {mai}Kg no: ', end='')
for i in list:
    if i[1] == mai:
        print(f'{i[0]}...', end='')
print()
print(f'A pessoa com menos peso é de {men}Kg no: ', end='')
for i in list:
    if i[1] == men:
        print(f'{i[0]}...', end='')
print()
