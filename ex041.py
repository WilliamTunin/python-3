n1 = float(input('Digite a primeira nota.'))
n2 = float(input('Digite a segunda nota.'))
m = (n1 + n2) / 2
print('Tirando {:.1F} e {:.1F}, a média do alune é {:.1f}'.format(n1, n2, m))
if 7> m >= 5:
    print('Você está de Recuperação')
elif m <5:
    print('Você está Reprovado.')
elif m >= 7:
    print('Você está Aprovado Parabens!!!!! .')
