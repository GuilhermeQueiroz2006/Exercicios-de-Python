
numero = 0
resposta = 'S'
divisor = 0
soma = 0
maior_numero = 0
quant_termos = 0

while resposta != 'N':
    quant_termos += 1
    divisor += 1
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()

    soma += numero

    if quant_termos == 1:
        maior_numero = menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero

        if numero < menor_numero:
            menor_numero = numero

media = soma / divisor

print(f'Você digitou {quant_termos} números e a média foi {media}')
print(f'O maior valor foi {maior_numero} e o menor foi {menor_numero}')
