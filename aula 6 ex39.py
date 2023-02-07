from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('quem nasceu em {} tem {} anos'.format(ano, idade))
if idade < 18:
    print('para completar 18 anos falta {} anos'.format(18 - idade))
elif idade == 18:
    print('voce serve o exercito este ano')
elif idade > 18:
    print('voce esta atrasado {} anos CORRE MLK'.format(idade - 18))
