sal = float(input('Qual é o seu salário atual R$'))
if sal > 1250.00:
    aum = sal + (sal * 10/100)
    print('Seu salário que era de R${:.2f} agora é de R${}'.format(sal, aum))
else:
    aum = sal + (sal * 15/100)
    print('Seu salário que era de R${:.2f} agora é de R${}'.format(sal, aum))
