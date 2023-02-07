listagem= ('Leite',3.50,'Pão',4.50,'Sacos de lixo',10.00,'Feijão',12.90,'Arroz',23.10,'Farinha de trigo',6.90,'Banana',4.90,)
print('-'*40)
print(f'\033[34m{"LISTA DE COMPRAS":^40}\033[m')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos %2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ' )
    else:
        print(f'{listagem[pos]:>5.2f}')
print('-'*40)