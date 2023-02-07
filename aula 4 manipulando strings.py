
nome=str(input('coloque seu nome:')).strip()
print('analizando seu nome...')
print('seu nome em maiusculo eh:{}'.format(nome.upper()))
print('seu nome em minusculo eh:{}'.format(nome.lower()))
print('o total de letras em seu nome sao:{}'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#=======================================================================================================================

num=int(input('digite um numero:'))
u=num // 1 % 10
d=num// 10%10
c=num//100%10
m=num//1000%10
print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(u,d,c,m))
#=======================================================================================================================
cidade=str(input('nome da cidade em que vc nasceu?')).strip()
print(cidade[:5].upper()=='SANTO')
#=======================================================================================================================
name=str(input('qual seu nome?')).strip()
print('seu nome tem silva? {}'.format('SILVA'in name.upper()))
#=======================================================================================================================
frase=str(input('digite uma frase:')).strip().lower()
print('a letra A aparece {} vezes'.format(frase.count('a')))
print('a primeira letra A apareceu na posicao {}'.format(frase.find('a')+1))
print('a ultima letra A apareceu na posicao {}'.format(frase.rfind('a')+1))
#=======================================================================================================================
n=str(input('digite seu nome completo:')).strip()
n1=n.split()
print('seu primeiro nome eh:{}'.format(n1[0]))
print('seu ultimo nome eh:{}'.format(n1[len(n1)-1]))
#=======================================================================================================================

