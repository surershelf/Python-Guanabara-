num = int(input('digite um numero: '))
print('\033[1;36m-=-=-=-=-\033[m' * 10)
print('\033[4;34m digite [1] para transformar em binario\033[m')
print('\033[4;33m digite [2] para transformar em octal \033[m')
print('\033[4;37m digite [3] para transformar em hexadecimal \033[m')
print('\033[1;36m -=-=-=-=- \033[m' * 10)
trans = int(input('escolha uma op;ao: '))
if trans == 1:
    a = bin(num)[2:]
    print(num, '=', a)
elif trans == 2:
    b = oct(num)[2:]
    print(num, '=', b)
elif trans == 3:
    c = hex(num)[2:]
    print(num, '=', c)
else:
    print('nao existe esta op;ao tente novamente')
