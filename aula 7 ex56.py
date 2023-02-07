somaidade=0
maioridadehomem = 0
nomevelho = ''
totmulher20=0
for c in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip().capitalize()
    idade = int(input('Idade da {} pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]: '.format(c))).lower().strip()
    print('\033[32m-=\033[m' * 25)
    somaidade+=idade
    if c==1 and sexo in 'm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'f' and idade > 20:
        totmulher20+=1
media = somaidade / 4
print('O grupo tem a media de {} anos'.format(media))
print('o homem mais velho eh o {},com {} anos'.format(nomevelho,maioridadehomem))
print('o total de mulheres com mais de 20 anos eh de {} mulheres'.format(totmulher20))

