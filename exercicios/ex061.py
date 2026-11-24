print('Gerador de PA')
print('-='*15)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
print(primeiro_termo, end=' -> ')
while c <= 10:
    c += 1
    resultado = primeiro_termo + razao
    print('{}'.format(resultado), end=' -> ')
    primeiro_termo = resultado
    resultado = primeiro_termo + razao
print('FIM')
