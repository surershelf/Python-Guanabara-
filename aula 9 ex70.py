print('='*30)
print('\033[33mSUPERMERCADO MAZZO\033[m')
print('='*30)
preço=m1000=barato=cont= 0
while True:
    a=str(input('Qual o nome do produto: '))
    b=int(input('Qual o preço do produto: '))
    preço+=b
    cont=+1
    nome=a
    if cont==1:
        barato=b
    else:
        if preço<barato:
            barato=b
    if b >= 1000:
        m1000+=1
    u=' '
    while u not in 'SN':
        u=str(input('Quer continuar ?[S/N] : ')).strip().upper() [0]
    if u =='N':
        break
print(f'O preço total da compra foi de R${preço}\n'
      f'Temos {m1000} produtos com o preço a mais de mil reais\n'
      f'E o produto mais barato é o {nome} custando {barato} ' )

