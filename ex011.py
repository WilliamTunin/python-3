l = float(input('Largura da parede:'))
h = float(input('Altura da parede:'))
a = l * h
n = a/2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(l, h, a))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(n))
