from random import randint

print('''Vamos Jogar Jokenpô
[1] Pedra
[2]Papel
[3]Tesoura
''')
voce = 0
ele = 0
while voce or ele != 3:
    a = int(input('Faça sua jogada: '))
    b = randint(1, 3)
    if a == 1:
        print('você escolheu Pedra')
        if b == 1:
            print('Seu adversário escolheu Pedra')
            print('Empate!')
        elif b == 3:
            print('\033[32mSeu adversário escolheu Tesoura')
            print('Ganhou!\033[m')
            voce += 1
        elif b == 2:
            print('\033[31mSeu adversário escolheu Papel')
            print('Perdeu!\033[m')
            ele += 1
    if a == 2:
        print('você escolheu Papel')
        if b == 2:
            print('Seu adversário escolheu Papel')
            print('Empate!')
        elif b == 1:
            print('\033[32mSeu adversário escolheu Pedra')
            print('Ganhou!\033[m')
            voce += 1
        elif b == 3:
            print('\033[31mSeu adversário escolheu Tesoura')
            print('Perdeu\033[m!')
            ele += 1
    if a == 3:
        print('você escolheu Tesoura')
        if b == 3:
            print('Seu adversário escolheu Tesoura')
            print('Empate!')
        elif b == 2:
            print('\033[32mSeu adversário escolheu Papel')
            print('Ganhou!\033[m')
            voce += 1
        elif b == 1:
            print('\033[31mSeu adversário escolheu Pedra')
            print('Perdeu!\033[m')
            ele += 1
if voce == 3:
    print('\033[32mParabéns, você ganhou!!!\033[m')
elif ele == 3:
    print('\033[31mPuxa, você perdeu\033[m')
