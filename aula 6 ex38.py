a = int(input('\033[32m primeiro valor: '))
b = int(input('\033[31m segundo valor:\033[m '))
if a > b:
    print('\033[32m o primeiro valor eh o maior')
elif b > a:
    print('\033[31m o segundo valor eh o maior\033[m')
else:
    print('\033[36m os 2 numeros tem o msm valor')
