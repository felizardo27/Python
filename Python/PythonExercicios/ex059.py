# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
print('\033[1;33m====== EX 059 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
from time import sleep
print('{}{}CALCULADORA{}{}'.format(cor['ciano'], '-='*5, '-='*5, cor['limpa']))
close = False
x = float(input('{}Primeiro valor:{} '.format(cor['ciano'], cor['limpa'])))
y = float(input('{}Segundo valor:{} '.format(cor['ciano'], cor['limpa'])))
while not close:
    print('''{}{}
        [ 1 ] Somar
        [ 2 ] multiplicar
        [ 3 ] subtrair
        [ 4 ] dividir
        [ 5 ] maior
        [ 6 ] novos números
        [ 7 ] sair do programa{}'''.format(cor['amarelo'], '-='*15, cor['limpa']))
    op = int(input('{}>>>>>>>>Qual a sua opção?{} '.format(cor['amarelo'], cor['limpa'])))
    if op == 1:
        res = x + y
        print('O resultado de {} + {} = {}'.format(x, y, res))
    elif op == 2:
        res = x * y
        print('O resultado de {} X {} = {}'.format(x, y, res))
    elif op == 3:
        res = x - y
        print('O resultado de {} - {} = {}'.format(x, y, res))
    elif op == 4:
        res = x / y
        print('O resultado de {} / {} = {}'.format(x, y, res))
    elif op == 5:
        if x > y:
            print('O valor {} é maior que o valor {}'.format(x, y))
        else:
            print('O valor {} é maior que o valor {}'.format(y, x))
    elif op == 6:
        print('Informe os números novamente: ')
        x = float(input('Primeiro valor: '))
        y = float(input('Segundo valor: '))
    elif op == 7:
        print('{}-={}'.format(cor['verde'], cor['limpa'])*15)
        print('{}FINALIZANDO...{}'.format(cor['verde'], cor['limpa']))
        print('{}-={}'.format(cor['verde'], cor['limpa'])*15)
        sleep(0.5)
        close = True
    else:
        print('OPÇÃO INVALIDA!!!!')
print('Fim do programa! Volte sempre!')

