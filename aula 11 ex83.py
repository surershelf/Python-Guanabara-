expr=str(input('Digite sua expressão: '))
pilha=[]
for simb in expr:
    if expr in '(':
        pilha.append('(')
    elif expr in ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')

