from ModulosTreino import moeda

p=float(input('Digite o preço: R$'))
print(f'A metade de {moeda.FormatMoeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.FormatMoeda(p)} é {(moeda.dobro(p,True))}')
print(f'Aumentando 10%, temos {moeda.aumentando(p,10,True)}')
print(f'Diminuindo 13%, temos {moeda.diminuindo(p,13, True)}')