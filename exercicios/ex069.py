tot_maiores = homem = mulher = 0

while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    print('-' * 30)

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if idade >= 18:
        tot_maiores += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulher += 1

    if escolha == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot_maiores}')
print(f'Ao todo temos {homem} homens cadastrados ')
print(f'E temos {mulher} mulher com menos de 20 anos ')
