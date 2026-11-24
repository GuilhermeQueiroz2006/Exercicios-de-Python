from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
esc = 0

while esc != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
        ''')
    esc = int(input('Qual a sua opção? '))
    if esc == 1:
        r = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, r))
    elif esc == 2:
        r = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, r))
    elif esc == 3:
        if n1 > n2:
            print('Entre {0} e {1} o maior valor é {0}'.format(n1, n2, ))
        elif n2 > n1:
            print('Entre {0} e {1} o maior valor é {1}'.format(n1, n2, ))
        else:
            print('Não valor maior entre {} e {}'.format(n1, n2))
    elif esc == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif esc == 5:
        print('Saindo do Sistema')
    else:
        print('Número inválido. Tente novamente')
    sleep(2)
