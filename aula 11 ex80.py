a=[]
for c in range (0,5):
    b = int(input('Digite um valor: '))
    if c == 0 or b > a[-1]:
        a.append(b)
        print('Item adicionado ao fim da lista')
    else:
        pos=0
        while pos<len(a):
            if b<= a[pos]:
                a.insert(pos,b)
                print(f'Adicionado a posição {pos} da lista')
                break
            pos+=1
print(f'voce digitou os seguintes numeros {a}')