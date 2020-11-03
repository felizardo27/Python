# Exercício Python 61: Refaça o DESAFIO 51,
# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('\033[1;33m====== EX 061 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
print('{}-={}'.format(cor['amarelo'], cor['limpa'])*15)
print('GERADOR DE PA')
print('{}-={}'.format(cor['amarelo'], cor['limpa'])*15)
t1= int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = t1
cont = 1
 # decimo termo
while  cont <= 10:
    print('{} -> '.format(t), end='')
    t += r
    cont += 1
print('FIM')
