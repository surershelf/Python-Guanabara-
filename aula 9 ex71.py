print('='*50)
print('\033[32mBanco Surershelf\033[m'.center(50))
print('='*50)
cedula=resto=a=0
while True:
    a=int(input('Quantos você quer sacar R$'))
    cedula=a//50
    resto=a%50
    print(f'Total de {cedula:.0f} cédulas de R$50')
    cedula=resto//20
    resto=resto%20
    print(f'Total de {cedula:.0f} cédulas de R$20')
    cedula=resto//10
    resto=resto%10
    print(f'Total de {cedula:.0f} cédulas de R$10')
    cedula=resto//1
    resto=resto%1
    print(f'Total de {cedula:.0f} cédulas de R$1')
    break
print('='*50)
print('\033[32mFIM VOLTE SEMPRE')

