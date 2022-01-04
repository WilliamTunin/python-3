dis = float(input('Qual a distancia da viagem?'))
print(' Você está prestes a começar uma viagem de {} KM'.format(dis))
'''if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45'''
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print(' O preço da sua passagem será de R${:.2f}'.format(preço))
