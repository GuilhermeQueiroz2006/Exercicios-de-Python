n1 = 0
n2 = 1
r = n1 + n2
termos = 0
c = 1

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

termos = int(input('Quantos termos você quer mostrar? '))

print('~'*35)
print(n1, n2, end=' -> ')
while c != termos:
    c += 1
    print(r, end=' -> ')
    n1 = n2
    n2 = r
    r = n1 + n2
print('FIM')
print('~'*35)
