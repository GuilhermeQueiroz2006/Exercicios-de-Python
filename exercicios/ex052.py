n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0 :
        print('\033[033m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[031m{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes '.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
