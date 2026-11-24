n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {} e {} sua média é {}'.format(n1, n2, m))
if m < 5.0:
    print('Sua média está abaixo de 5.0: REPROVADO')
elif m >= 5.0 and m < 6.9:
    print('Sua média está entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    print('Sua média é superior a 7.0: APROVADO')
