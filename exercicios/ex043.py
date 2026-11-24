altura = float(input('Informe sua altura (m): '))
peso = float(input('Informe seu peso (kg): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('''O seu IMC é de {:.1f}
     Classificação: ABAIXO DO PESO'''.format(imc))
elif imc < 25:
    print('''O seu IMC é de {:.1f}
    Classificação: PESO IDEAL'''.format(imc))
elif imc < 30:
    print('''O seu IMC é de {:.1f}
    Classificação: SOBREPESO'''.format(imc))
elif imc < 40:
    print('''O seu IMC é de {:.1f}
    Classificação: OBESIDADE'''.format(imc))
else:
    print('''O seu IMC é de {:.1f}
    Classificação: OBESIDADE MÓRBIDA''')
