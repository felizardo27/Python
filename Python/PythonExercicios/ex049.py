# Exercício Python 49: Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
print('\033[1;33m====== EX 049 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
print('{}-={}'.format(cor['vermelho'], cor['limpa'])*12)
print('{}      TABUADA 2.0      {}'.format(cor['amarelo'], cor['limpa']))
print('{}-={}'.format(cor['vermelho'], cor['limpa'])*12)
n = int(input('{}Digite um número para ver sua tabuada: {}'.format(cor['ciano'], cor['limpa'])))
for x in range(1, 11):
    print('{}{} X {:2} = {}{}'.format(cor['verde'], n, x, x*n, cor['limpa']))
