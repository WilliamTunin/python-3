peso = float(input('Qual o seu peso ? (KG)'))
altura = float(input('Qual é sua altura ? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1F}'.format(imc))
if imc < 18.5:
    print('Você está abaico do peso normal.')
elif 18.5 <= imc < 25:
    print('Parabens você está na faixa de peso normal.')
elif 25 <= imc < 29.9:
    print('Você está em sobrepeso.')
elif 30 <= imc < 34.9:
    print('Você está em Obeidade Tipo I.')
elif 35 <= imc < 39.9:
    print('Voce está em Obesidade tipo II.')
elif imc >= 40:
    print('Você está em Obesidade Morbida CUIDADO !!!.')
