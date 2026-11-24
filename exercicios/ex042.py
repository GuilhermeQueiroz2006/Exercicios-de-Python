n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Não é possível formar um triângulo com esses segmentos!')
