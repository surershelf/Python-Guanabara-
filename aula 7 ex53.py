frase=str(input('digite uma frase: ')).strip().upper()
palavra=frase.split()
junto=''.join(palavra)
inverso=''
for letras in range(len(junto) - 1,-1,-1):
    inverso += junto[letras]
print('O inverso de {} eh {}'.format(junto,inverso))
if inverso == junto:
    print('Achamos um Palindromo!')
else:
    print('Isto nao eh um Palindromo')