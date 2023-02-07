def ficha(nome='',g=0):
    if nome=='':
        nome ='<desconhecido>'
    return f'O jogador {nome} fez {g} gol(s)'


n=str(input('Qual o nome do jogador: '))
g=str(input('Quantos gols ele fez: '))
if g.isnumeric():
    g=int(g)
else:
    g=0
print(ficha(n,g))
