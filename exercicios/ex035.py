print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
l1 = int(input('Digite o primeiro valor: '))
l2 = int(input('Digite o segundo valor: '))
l3 = int(input('Digite o terceiro valor: '))
if (l1 < l2+l3) and (l2 < l1+l3) and (l3 < l1+l2):
    print('Um Triângulo PODE ser formado por estes valores ')
else:
    print('Um Triângulo NÃO PODE ser formado por estes valores')
