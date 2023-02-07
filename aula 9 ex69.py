print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
p=m18=h=f20=0
while True:
    i=int(input('Qual a idade: '))
    s=str(input('Sexo [M/F]: ')).strip().upper()
    p+=1
    if i >= 18:
        m18+=1
    if s in 'Mm':
        h+=1
    if s in 'Ff' and i >= 20:
        f20+=1
    print('-'*30)
    c=str(input('Quer continuar [S/N]: ')).strip().upper()
    print('-' * 30)
    if c in 'nN':
        break
print(f'''Foram cadastradas um total de {p} pessoas
Temos {m18} pessoas maior de 18 anos
Foram cadastrados {h} homens
Temos {f20} mulheres com mais de 20 anos ''')
