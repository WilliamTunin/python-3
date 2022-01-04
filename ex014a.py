n = float(input('Valor do Produto: R$'))
a = n - (n * 10 / 100)
c = n + (n * 8 / 100)
print('O valor do produto é {:.2f}. \nNo boleto tem 10% de desconto {:.2f}. \nParcelado custa {:.2f}'.format(n, a, c))
