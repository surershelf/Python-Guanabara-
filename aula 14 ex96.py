def area(l,c):
    print(f'A área de um terreno {l} x {c} é de {l*c:.2f}m²')


print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
l=float(input('Digite a largura: '))
c=float(input('Digite o comprimento: '))
area(l,c)

