from math import hypot
'''op = float(input("Digite o cateto oposto: "))
ad = float(input("Digite o cateto adjacente: "))
hip = (op ** 2 + ad ** 2) ** (1/2)
print("A hipotenusa de {} com {} é {}!".format(ad, op, hip))'''
op = float(input("Digite o cateto oposto: "))
ad = float(input("Digite o cateto adjacente: "))
hi = hypot(op, ad)
print("A hipotenusa é: {:.2f}".format(hi))
