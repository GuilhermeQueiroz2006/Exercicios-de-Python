D = int(input("Digite a quantidade de dias: "))
KM = float(input("Digite os KM percorridos: "))
A = (D * 60) + (KM * 0.15)
print("O valor total a se pagar do aluguel será de R${:.2f}".format(A))
