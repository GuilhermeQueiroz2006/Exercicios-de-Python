from datetime import date
nasc = int(input('Ano de Nascimento: '))
idade = date.today().year - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificaçâo: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
