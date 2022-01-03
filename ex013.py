n = float(input('Salario do funcionario: R$'))
r = n + (n*15/100)
print('Reajuste do salario R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(n, r))
