b = int(input('Digite um numero de 0 a 20: '))
while True:
   a = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenovo', 'Vinte')
   if b<0 or b>20:
      b= int(input('Tente novamente, este número não está no combinado: '))
   elif b>=0 or b<20:
      c=a [b]
      print(f'Voce escolheu o numero {c} ')
      break

