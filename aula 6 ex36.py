a = float(input('qual o valor da casa: '))
b = float(input('qual o valor do seu salario: '))
c = int(input('em quantos anos ira pagar: '))
mes = c * 12
prest = a / mes
minimo = b * 30 / 100
print('para pagar uma casa de {:.2f} em {} anos '.format(a, c))
print(''''a prestaçao será de R${:.2f} e o seu minimo é de R${}
⠄⠄⠄⢠⣶⣶⣦⣤⣶⣦⣤⣶⣶⣤⡄⠄⡆⠄
⠄⣂⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⡆⠄
⢠⢻⣿⡿⣟⡛⠻⢿⣿⣿⡿⠿⠟⠻⢿⣿⣇⠄
⢀⣺⣿⡟⠋⡉⢉⠚⢿⣿⠗⢊⠙⡛⢿⣿⡌⠄
⠈⣝⣿⣿⣿⣧⣤⣤⣿⣿⣶⣤⣼⣿⣿⣿⡇⠄
⠄⠙⣿⣿⣿⣿⣿⡿⣿⣿⣷⣿⣿⣿⣿⡟⠄⠄
⠄⠄⣿⣿⣿⠛⣋⣩⣬⣥⣤⡍⢙⣿⣿⡇⠄⠄
⠄⠄⠘⣿⣿⣴⣭⣿⣿⣿⣿⣵⣾⣿⠏⠄⠄⠄
⠄⠄⠄⣿⣿⣿⣿⣷⣤⣴⣿⣿⣿⣿⠄⣠⠤⠄
⢀⠄⠚⣿⣿⣷⡌⣁⣀⣀ '''''.format(prest, minimo))
if prest <= minimo:
    print('\033[32m vc pode comprar e pagar as parcelas\033[m')
else:
    print('\033[31m vc nao pode comprar a casa\033[m')
