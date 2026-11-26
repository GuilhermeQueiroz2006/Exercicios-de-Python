numeros_extenso = ('zero', 'um', 'dois', 'três',
    'quatro', 'cinco', 'seis', 'sete',
    'oito', 'nove', 'dez', 'onze',
    'doze', 'treze', 'catorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove',
    'vinte')


while True:
    numero = int(input('Digite um número: '))
    escolha = ' '

    if 0 <= numero <= 20:
        print(f'O número digitado foi {numeros_extenso[numero]}')

        while escolha not in 'SN':
            escolha = str(input('Quer continua? [S/N]: ')).upper().strip()

        if escolha == 'N':
            print('Finalizando Processo...')
            break

    else:
        print('Tente Novamente', end=' ')
