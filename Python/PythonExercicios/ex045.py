# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
print('\033[1;33m====== EX 045 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
import time
import random
print(f'\033[1;33m{" JOKENPÔ ":=^40}\033[m')
m = random.choice(['pedra', 'papel', 'tessoura']).upper()
print('''{}Suas opções: {}
{}[ 0 ] - PEDRA 
[ 1 ] - PAPEL
[ 2 ] - TESSOURA{}'''.format(cor['ciano'], cor['limpa'], cor['amarelo'], cor['limpa']))
op = int(input('{}Qual é sua jogada? {}'.format(cor['ciano'], cor['limpa'])))
if op != 0 and op != 1 and op != 2:
    print('{}OPCÇÃO INVALIDA!!!'.format(cor['vermelho'], cor['limpa']))
    exit()
print('{}JO{}'.format(cor['verde'], cor['limpa']))
time.sleep(1)
print('{}KEN{}'.format(cor['verde'], cor['limpa']))
time.sleep(1)
print('{}PO!!!{}'.format(cor['verde'], cor['limpa']))
time.sleep(1)
print('{}-={}'.format(cor['amarelo'], cor['limpa'])*15)
print('{}   Computador jogou {}{}'.format(cor['ciano'], m, cor['limpa']))
if op == 0:
    print('{}   Jogador jogou PEDRA{}'.format(cor['ciano'], cor['limpa']))
    print('{}-={}'.format(cor['amarelo'], cor['limpa']) * 15)
    if m == 'PEDRA':
        print('{}EMPATE!{}'.format(cor['azul'], cor['limpa']))
    elif m == 'PAPEL':
        print('{}COMPUTADOR VENCEU!{}'.format(cor['vermelho'], cor['limpa']))
    elif m == 'TESSOURA':
        print('{}JOGADOR VENCEU!{}'.format(cor['verde'], cor['limpa']))
elif op == 1:
    print('{}   Jogador jogou PAPEL{}'.format(cor['ciano'], cor['limpa']))
    print('{}-={}'.format(cor['amarelo'], cor['limpa']) * 15)
    if m == 'PEDRA':
        print('{}JOGADOR VENCEU!{}'.format(cor['verde'], cor['limpa']))
    elif m == 'PAPEL':
        print('{}EMPATE!{}'.format(cor['azul'], cor['limpa']))
    elif m == 'TESSOURA':
        print('{}COMPUTADOR VENCEU!{}'.format(cor['vermelho'], cor['limpa']))
elif op == 2:
    print('{}   Jogador jogou TESSOURA{}'.format(cor['ciano'], cor['limpa']))
    print('{}-={}'.format(cor['amarelo'], cor['limpa']) * 15)
    if m == 'PEDRA':
        print('{}COMPUTADOR VENCEU!{}'.format(cor['vermelho'], cor['limpa']))
    elif m == 'PAPEL':
        print('{}JOGADOR VENCEU!{}'.format(cor['verde'], cor['limpa']))
    elif m == 'TESSOURA':
        print('{}EMPATE!{}'.format(cor['azul'], cor['limpa']))

