from random import randint

numero_computador = randint(0, 10)
total_escolhas = 1

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

numero_pessoa = int(input('Qual é seu palpite? '))
while numero_pessoa != numero_computador:
    total_escolhas += 1
    if numero_pessoa < numero_computador:
        numero_pessoa = int(input('Mais... Tente mais uma vez: '))
    else:
        numero_pessoa = int(input('Menos... Tente mais uma vez: '))


print('ACERTOU!!! O número escolhido era {}'.format(numero_computador))
print('Acertou com {} tentativas. Parabéns!'.format(total_escolhas))
