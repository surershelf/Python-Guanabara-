def notas(*n,sit=False):
    """
    -> Função para analisar notas e situações dos alunos
    :param n: AQUI SERA ATRIBUIDA A NOTA DO ALUNO
    :param sit: PARA MOSTRAR OU NÃO A SITUAÇÃO DA MÉDIA DE NOTAS
    :return: IRÁ RETORNAR O DIC ALUNOS
    Criado por Lucas Mazzo ou Surershelf
    """
    mai=st=0
    men=10
    alunos = {'QuantNotas': '', 'MaiNota': '', 'MenNota': '', 'Media': '', 'Situacao': ''}
    alunos['QuantNotas']=len(n)
    for c in n:
        if c>mai:
            mai=c
            alunos['MaiNota']=mai
        if c<men:
            men=c
            alunos['MenNota']=men
    for c in n:
        st+=c
        alunos['Media']=st/len(n)
    if sit==True:
        alunos['Situacao']=alunos['Media']
        if alunos['Situacao']>=7:
            alunos['Situacao']='SITUAÇÃO BOA'
        elif alunos['Situacao']> 6 and alunos['Situacao'] < 7:
            alunos['Situacao']='SITUAÇÃO RAZOÁVEL'
        elif alunos['Situacao']<6:
            alunos['Situacao']='SITUAÇÃO RUIM'
    elif sit==False:
        del alunos['Situacao']
    return alunos


resp=notas(7,8,10,5,9,4,7,9,sit=True)
print(resp)
help(notas)
#GUANABARA USOU O MODO MAIS FACIL
#ELE USOU OS METODOS SUM() PARA SOMAR MAX() PARA PEGAR O MAIOR E MIN() PARA O MENOR