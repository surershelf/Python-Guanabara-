pessoa={'nome':'','media':'','situação':''}
pessoa['nome']=str(input('Digite o nome da pessoa: '))
pessoa['media']=float(input(f'Digite a media de {pessoa["nome"]}: '))
if pessoa['media'] >= 7:
    pessoa['situação']= 'APROVADO'
else:
    pessoa['situação']= 'REPROVADO'
print(f'A situação do {pessoa["nome"]} é {pessoa["situação"]}')