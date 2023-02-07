a=('aprender','ensinar','jogar','bater','voar','ponta','matue','comercial')
for palavra in a:
    print(f'\nNa palavra {palavra.upper()} tem as seguintes vogais :',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print (letra,end=' ')




