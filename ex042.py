from datetime import date
atual = date.today().year
ano = int(input("qual o ano de nascimento do atelta ?"))
idade = atual - ano
print('O Atleta nascido em {} tem {} anos.'.format(ano, idade))
if idade <= 9:
    print('Clasificaçâo: Mirim.')
elif idade <= 14:
    print('Clasificação: Infantil.')
elif idade <= 19:
    print('Clasificaçâo: Júnior.')
elif idade <= 25:
    print('Clasificaçâo: Sênior.')
else:
    print('Clasificação: Master.')
