from time import sleep
N = str(input('Digite seu nome: ')).strip()
NS = N.split()
(print('Analisando seu nome...'))
sleep(2)
print('Seu nome em maiúsculo é {}'.format(N.upper()))
print('Seu nome em minúsculas é {}'.format(N.lower()))
print('Seu nome tem ao todo {} letras'.format(len(N) - N.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(NS[0], len(NS[0])))
