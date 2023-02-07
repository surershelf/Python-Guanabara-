def voto(ano):
    from datetime import date as dt
    b=dt.today().year
    c=b-a
    print(f'Com {c} anos, ',end='')
    if c < 18:
        return f'AINDA NÃO VOTA'
    elif c>=18 and c<65:
        return f'O VOTO É OBRIGATÓRIO'
    elif c>=65:
        return f'O VOTO É OPCIONAL'




a=int(input(f'Em que ano você nasceu? '))
print(voto(a))