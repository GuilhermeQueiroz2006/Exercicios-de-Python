print('Gerador de PA')
print('-='*15)


primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))


c = 1
quant_termos = 10
total = 0

print(primeiro_termo, end=' -> ')
while quant_termos != 0:
    total += quant_termos
    while c <= total:
        c += 1
        resultado = primeiro_termo + razao
        print('{}'.format(resultado), end=' -> ')
        primeiro_termo = resultado
        resultado = primeiro_termo + razao
    quant_termos = int(input('Pausa \nQuantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')
