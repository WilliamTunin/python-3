vel = float(input('Qual é a velocidade do carro? '))
if vel > 80:
    print('MULTADO! Você execedeu o limite permitido que é 80KM/H')
    multa = (vel-80) * 7
    print(' Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
