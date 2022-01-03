import math
from math import sin, cos, tan
an = float(input('Digite um ângulo que você deseja'))
s = sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, s))
c = cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, c))
t = tan(math.radians(an))
print('O ângulo digitado {} tem a tangente de {:.2f}'.format(an, t))
