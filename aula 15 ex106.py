from time import sleep
color = {'clear': '\033[m', 'green': '\033[1;42m', 'blue': '\033[1;46m', 'white': '\033[1;30;107m', 'red': '\033[1;41m'}


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',cor='blue')
    print(color['white'],end='')
    help(com)
    print(color['clear'],end='')
    sleep(2)

def titulo(msg, cor='clear'):
    tam = len(msg) + 4
    print(f'{color[cor]}', end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(f'{color["clear"]}', end='')
    sleep(1)


comando = ''
while True:
    titulo('Sistema De Ajuda PyHelp', cor='green')
    comando = str(input('Função ou Biblioteca >  '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!',cor='red')
