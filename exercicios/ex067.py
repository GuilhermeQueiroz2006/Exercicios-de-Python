while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-' * 35)
    for c in range(1, 11):
        r = n * c
        print(f'{n:2} x {c:2} = {r}')
    print('-' * 35)