m = float(input('Digite o tamanho em metros: '))
cm = m*100
mm = m*1000
km = m/1000
hm = m/100
dam = m/10
dm = m*10
print('O valor de {}m correspode a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, km, hm, dam, dm, dm, mm))
