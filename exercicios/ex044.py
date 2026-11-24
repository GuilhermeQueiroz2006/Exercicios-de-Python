print('{:=^40}'.format(' LOJAS QUEIROZ '))
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
esc = int(input('Digite a opção: '))
if esc == 1:
    valor_final = compras - (compras * 10/100)
    print('Sua compra será paga a vista no dinheiro/cheque')
    print('A compra de valor R${:.2f} ficará R${:.2f} com 10% de desconto'.format(compras, valor_final))
elif esc == 2:
    valor_final = compras - (compras * 5/100)
    print('Sua compra será paga a vista no cartão')
    print('A compra no valor de R${:.2f} ficará R${:.2f} com 5% de desconto'.format(compras, valor_final))
elif esc == 3:
    parcelas = compras / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcelas))
    print('A compra no valor de R${:.2f} não terá alterações'.format(compras))
elif esc == 4:
    quant_parcelas = int(input('Quantas parcelas: '))
    valor_final = compras + (compras * 20/100)
    parcelas = valor_final / quant_parcelas
    print('Sua compra será em {}x de R${} COM JUROS'.format(quant_parcelas, parcelas))
    print('A compra de R${} vai custar R${} no final'.format(compras, valor_final))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO')
