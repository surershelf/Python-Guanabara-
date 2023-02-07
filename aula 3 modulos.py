import math
num=float(input('digite um numero:'))
inteiro=math.trunc(num)
print('a por;ao inteira de {} eh {}'.format(num,inteiro))
#===================================trunc serve pra corta o numero =================================================
co=float(input('comprimento do cateto oposto: '))
ca=float(input('comprimento do cateto adjacente: '))
hip=math.hypot(co,ca)
print('a hipotenusa tem que medir {:.2f}'.format(hip))
#========================================para medir hipotenusa======================================================
ang=float(input('digite o angulo que vc qr medir: '))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tang=math.tan(math.radians(ang))
print('do angulo de {} o SENO eh {:.2f}'.format(ang,sen))
print('do angulo de {} o COSSENO eh {:.2f}'.format(ang,cos))
print('do angulo de {} o TANGENTE eh {:.2f}'.format(ang,tang))
#===================================================================================================================
import random
n1=str(input('nome do aluno: '))
n2=str(input('nome do aluno: '))
n3=str(input('nome do aluno: '))
n4=str(input('nome do aluno: '))
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
#================================para fazer uma escolha de uma lista================================================
ordem=random.shuffle(lista)
print('a ordem de apresenta;ao eh:')
print(lista)
#==========================================embaralha a ordem========================================================



