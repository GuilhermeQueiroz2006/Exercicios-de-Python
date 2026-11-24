from datetime import date
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Você é homem ou mulher [M/F]: ').isupper())
idade = date.today().year - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, date.today().year))
if sexo == 'F':
    print('O alistamento é obrigatório apenas para homens')
elif idade < 18 and sexo == 'M':
    alist = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(alist))
    print('Seu alistamento será em {}.'.format(date.today().year + alist))
elif idade == 18 and sexo == 'M':
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18 and sexo == 'M':
    alist = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(alist))
    print('Seu alistamento foi em {}'.format(date.today().year - alist))
