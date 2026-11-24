from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
nm = randint(0,5)
ne = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if ne == nm:
    print('PARABÉNS VOCÊ ACERTOU!!!')
else:
    esc = str(print('Você errou, o número pensado foi {}. Tente novamente!'.format(nm)))
