from random import randint

ganhou = 0

print('-=' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 15)

while True:

    jogador = int(input('Diga um valor: '))
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = str(input('Par ou Ímpar [P/I]: ')).upper().strip()

    computador = randint(1, 11)
    total = jogador + computador

    if total % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {total} DEU PAR')
        print('-' * 20)

        if par_impar == 'P':
            print('VOCÊ VENCEU!!!')
            print('Vamos jogar novamente...')
            ganhou += 1

        else:
            print('VOCÊ PERDEU')
            print('-=' * 20)
            print(f'GAME OVER! Você venceu {ganhou} vezes.')
            break


    else:
        print('-' * 20)
        print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {total} DEU ÍMPAR')
        print('-' * 20)

        if par_impar == 'I':
            print('VOCÊ VENCEU!!!')
            print('Vamos jogar novamente...')
            ganhou += 1

        else:
            print('VOCÊ PERDEU')
            print('-=' * 20)
            print(f'GAME OVER! Você venceu {ganhou} vezes.')
            break
