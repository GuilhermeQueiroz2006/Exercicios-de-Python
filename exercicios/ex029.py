vel = int(input('Qual a velocidade atual de seu carro? '))
mul = (vel - 80) * 7
if vel <= 80:
    print('Continue dirigindo com segurança!')
else:
    print('INFRAÇÃO GRAVE')
    print('Multa de R${:.2f}'.format(mul))
