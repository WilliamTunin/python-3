print('-=-*20')
print('Analizador de triângulos')
print('-=-*20')
r1 = float(input('Qual a primeiro reta? '))
r2 = float(input('Qual a segunda reta? '))
r3 = float(input('Qual a terceira reta? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulos!')
else:
    print('Os segumentos acima NÂO podem formar um triângulo!')
