cont = a = soma = 0
while True:
    a = (int(input('Digite um valor \033[31m [999 para parar] \033[m :')))
    if a == 999:
        break
    soma += a
    cont += 1
print(f'Você digitou {cont} números e a soma deles são {soma}')
