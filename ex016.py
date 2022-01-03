d = int(input('Quantos dia de Locação? '))
km = float(input('Quantos Km rodados? '))
v = (d * 60) + (km * 0.15)
print('Valor total da locação é de R${:.2f}'.format(v))
