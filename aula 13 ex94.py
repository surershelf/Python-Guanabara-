pessoa= { }
galera= []
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp=='N':
        break
print('=-'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media=soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos ')
print(f'As mulheres cadastradas foram',end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ',end='')
print()
print('Lista das pessoas acima da média',end='')
for p in galera:
    if p['idade']>= media:
        print('     ')
        for k,v in p.items()
            print(f'{k} = {v}; ',end='')
print('<< ENCERRADO >>')
