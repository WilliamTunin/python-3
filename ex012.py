n = float(input('Valor do produto? R$'))
d = n - (n * 5 / 100)
print('O produto que custa R${:.2f} na promoção com desconto de 5% custa R${:.2f}'.format(n, d))
