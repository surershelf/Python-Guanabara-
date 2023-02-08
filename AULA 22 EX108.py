from ModulosTreino import moeda

p=float(input('Digite o preço: R$'))
print(f'A metade de {moeda.FormatMoeda(p)} é {moeda.FormatMoeda(moeda.metade(p))}')
print(f'O dobro de {moeda.FormatMoeda(p)} é {moeda.FormatMoeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.FormatMoeda(moeda.aumentando(p,10))}')
print(f'Diminuindo 13%, temos {moeda.FormatMoeda(moeda.diminuindo(p,13))}')