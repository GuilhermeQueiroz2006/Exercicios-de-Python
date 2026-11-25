tot_compra = caro = mais_barato = cont = 0

print('-' * 30)
print('     LOJA SUPER BARATÃO')
print('-' * 30)

while True:
    nome_produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    tot_compra += preco
    cont += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()

    if cont == 1:
        mais_barato = preco
        produto_mais_barato = nome_produto

    if preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = nome_produto

    if preco >= 1000:
        caro += 1

    if continuar == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot_compra}')
print(f'Temos {caro} produto custando mais de R$1000.00')
print(f'A compra mais bara foi {produto_mais_barato} e custou R${mais_barato}')