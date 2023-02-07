print('{:=^40}'.format(' LOJAS SURERSHELF '))
compras = float(input('Qual o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao 
[ 4 ] 3x ou mais no cartao''')
opçao = int(input('qual a opçao de pagamento: '))
if opçao == 1:
    total = compras - (compras * 10 / 100)
elif opçao == 2:
    total = compras - (compras * 5 / 100)
elif opçao == 3:
    total = compras
    parcela = total / 2
    print('Sua parcela de 2x vai custar R${:.2f} cada uma SEM JUROS'.format(parcela))
elif opçao == 4:
    total = compras + (compras * 20 / 100)
    totparc = int(input('Quantas parcelas vc vai pagar: '))
    parcela = total / totparc
    print('Sua compra vai ser divida em {}x e ira custar R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = compras
    print('\033[31m ERRO, nao existe esta opçao de pagamento tente novamente.\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compras, total))
