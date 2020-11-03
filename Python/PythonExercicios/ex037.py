# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('\033[1;33m====== EX 037 ======\033[m')
cor = {'limpa': '\033[m',
       'azul': '\033[1;34m',
       'amarelo': '\033[1;33m',
       'vermelho': '\033[1;31m',
       'verde': '\033[1;32m'}
n = int(input('{}Digite um número inteiro: {}'.format(cor['azul'], cor['limpa'])))

print('{}Escolha uma das bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter HEXADECIMAL{}'.format(cor['verde'], cor['limpa']))
op = int(input('{}Sua opção: {}'.format(cor['verde'], cor['limpa'])))
if op == 1:
    print('{}{} convertido para BINÁRIO é igual a {}{}'.format(cor['amarelo'], n, bin(n)[2:], cor['limpa']))
elif op == 2:
    print('{}{} convertido para OCTAL é igual a {}{}'.format(cor['amarelo'], n, oct(n)[2:], cor['limpa']))
elif op == 3:
    print('{}{} convertido para HEXADECIMAL é igual a {}{}'.format(cor['amarelo'], n, hex(n)[2:], cor['limpa']))
else:
    print('{}OPÇÃO INVALIDA!{}'.format(cor['vermelho'], cor['limpa']))