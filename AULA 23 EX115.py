from ModulosTreino.dados import *
from ModulosTreino.arquivo import *
from time import sleep

arq='cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta=menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta==1:
        #opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta==2:
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta==3:
        cabecalho('Saindo do sistema... Até mais!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)