from time import sleep


def maior(*num):
    print('-'*40)
    for v in num:
        sleep(0.5)
        print(f' {v} ',end='')
    print(f', foram digitados {len(num)} números')
    mai=0
    for c in num:
        if c>=mai:
            mai=c
    print(f'O maior número digitado foi {mai}')


maior(4,6,7,4,2)
maior(4,8,5,9,20,320,12,5,6,7)

