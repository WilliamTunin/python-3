import random

n1 = str(input('Primeiro Nome'))
n2 = str(input('Segundo Nome'))
n3 = str(input('Terceiro Nome'))
n4 = str(input('Quarto Nome'))
list = [n1, n2, n3, n4]
random.shuffle(list)
print('A ordem de apresentação será ')
print(list)