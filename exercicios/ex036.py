valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Qual é o seu salário: R$'))
anos = int(input('Quantos anos de financiamento: '))
pres = valor_casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, anos, pres))
if pres >= salario * 30/100:
    print('Pedido de empréstimo NEGADO!')
else:
    print('Pedido de emprétimo APROVADO')
