somaidade = 0
mulher = 0
maior_idade = 0
for c in range(1, 5):
    print('---- {}° PESSOA ----'.format(c))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())
    somaidade += idade
    if sexo == 'M' and maior_idade < idade:
        maior_idade = idade
        nome_mais_velho = nome

    if sexo == 'F' and idade <= 20:
        mulher += 1
media = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
