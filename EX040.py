from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento'))
sex = str(input('Qual o seu sexo ? Homem ou Mulher [H/M]')).strip().lower()
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif sex == 'm':
    print('Pela Lei Brasileira o alistamento é obrigatorio somente para homens.')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print(' Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
