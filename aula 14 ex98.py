from time import sleep


def contador(i,f,p):
    print('-'*40)
    if p<0:
        p*=-1
    if p==0:
        p=1
    print(f'A contagem vai de {i} para {f} de {p} em {p}')
    if i<f:
        cont=i
        while cont <= f:
            print(f'{cont} => ',end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont=i
        while cont>=f:
            print(f'{cont} => ',end='')
            sleep(0.5)
            cont-=p
        print('FIM')


contador(1,10,1)
contador(10,0,2)
print('-'*40)
print('Agora é sua vez')
ini=int(input('Digite que número começar: '))
fim=int(input('Digite onde parar: '))
pas=int(input('de qunatos em quantos vai pular: '))
contador(ini,fim,pas)