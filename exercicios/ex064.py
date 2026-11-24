numero = 0
tot_numeros = 0
soma = 0

numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    tot_numeros += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {tot_numeros} números e a soma entre eles foi {soma}')