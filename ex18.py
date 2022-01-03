import math
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('QUal o valor do cateto adjacnte? '))
hy = math.hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hy))

