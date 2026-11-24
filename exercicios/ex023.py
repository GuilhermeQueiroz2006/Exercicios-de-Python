from time import sleep
N = int(input('Informe um número: '))
u = N // 1 % 10
d = N // 10 % 10
c = N // 100 % 10
m = N // 1000 % 10
print('Analisando o número {}'.format(N))
sleep(2)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
