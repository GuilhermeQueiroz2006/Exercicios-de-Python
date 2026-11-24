from datetime import date
menor = 0
maior = 0
atual = date.today().year
for pess in range(1, 8):
    ano_nasc = int(input('Em que ano a {}.o pessoa nasceu? '.format(pess)))
    idade = atual - ano_nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade!'.format(maior))
print('E também tivemos {} pessoas menores de idade!'.format(menor))
