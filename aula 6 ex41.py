i = int(input('qual sua idade: '))
if i <= 9:
    print('voce esta na categoria mirim')
elif i <= 14:
    print('vc esta na categoria infantil')
elif i <= 19:
    print('vc esta na categoria junior')
elif i == 20:
    print('vc esta na categoria senior')
else:
    print('vc esta na categoria master')
