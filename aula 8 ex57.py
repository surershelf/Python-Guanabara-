a = str(input('Qual seu Sexo? [M/F]  ')).strip().upper()
while a not in 'FfMm':
    a=str(input('este sexo nao existe tente novamente: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(a))
