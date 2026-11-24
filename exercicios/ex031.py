V = int(input('De quantos KM será a sua viagem: '))
if V > 200:
    C = V * 0.45
    print('O custo total de sua viagem de {}KM será de R${:.2f} com o desconto de viagens acima de 200KM'.format(V, C))
else:
    C = V * 0.50
    print('O custo total de sua viagem de {}KM será de R${:.2f}'.format(V, C))
print('Obrigado por viajar conosco!')
'''
C = V * 0.50 if V <= 200 else C = V * 0.45
'''
