# 1 ler o nome, data de nascimento e carteira de trabalho da pessoa e adicionar no dicionario
import datetime as dt
cad={'nome':' ','idade':' ','ctps':'','ano_contratado':'','aposentadoria':'' }
cad['nome']=str(input('Nome: ')).capitalize()
a=cad['idade']=int(input('Ano de nascimento: '))
atual=dt.date.today().year
cad['idade']= atual-a
cad['ctps']=int(input('Carteira de Trabalho [digite 0 caso não tenha]: '))
if cad['ctps'] != 0:
    cad['ano_contratado']=int(input('Ano da Contratação: '))
    c=atual-cad['ano_contratado']
    cad['aposentadoria']= cad['ano_contratado'] +35
    cad['aposentadoria']=cad['aposentadoria']+cad['idade']
    cad['aposentadoria']=cad['aposentadoria']-atual
else:
    cad.pop('ano_contratado')
    cad.pop('aposentadoria')
print('-='*30)
for i,v in cad.items():
    print(f'{i} tem o valor de: {v}')