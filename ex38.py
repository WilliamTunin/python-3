num = int(input(' Digite o numero que deseja trocar de base: '))
base = int(input(''' Escolha o tipo de base a ser convertida:
Binaria digite: 1
Octal digite: 2
Hexadecimal Digite: 3

Sua escolha: \n'''))
if base == 1:
    print('A base escolhida foi Binaria')
    print('{} convertido para base Binaria fica {} '.format(num, bin(num)[2:]))
elif base == 2:
    print('A base escolhida foi Octal')
    print('{} convertido pasa base Octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('A base escolhida foi Hexadecimal')
    print('{} convertido para base Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. tente novamente ')
