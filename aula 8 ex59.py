
print('''\033[36m[1] Soma
[2] Multiplicação
[3] Qual o maior
[4] Escreva novos numeros
[5] Sair do jogo \033[m''')
acertos = 0
erros = 0
a = int(input('\nSelecione uma opção: '))
b = int(input('Escreva um numero:'))
c = int(input('escreva outro numero:'))
while a != 5:
    if a == 1:
        resposta = b + c
        print(b, '+', c, '=', resposta)
        a = int(input('selecione uma opção: '))
    elif a == 2:
        resposta = b * c
        print(b, 'x', c, '=', resposta)
        a = int(input('selecione uma opção: '))
    elif a == 3:
        if b > c:
            print('o numero {} eh maior que o {}'.format(b, c))
            a = int(input('selecione uma opção: '))
        elif c > b:
            print('o numero {} eh maior que o {}'.format(c, b))
            a = int(input('selecione uma opção: '))
        else:
            print('os dois valores sao iguais')
            a = int(input('selecione uma opção: '))
    elif a == 4:
        b = int(input('Escreva um novo numero: '))
        c = int(input('escreva outro novo numero: '))
        a = int(input('selecione uma opção: '))
print('fim')
