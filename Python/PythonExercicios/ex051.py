# Exercício Python 51: Desenvolva um programa que leia 
# o primeiro termo e a razão de uma PA. No final, 
# mostre os 10 primeiros termos dessa progressão.
print('\033[1;33m====== EX 051 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
print('{}-={}'.format(cor['amarelo'], cor['limpa'])*15)
print('10 TERMOS DE UMA PA')
print('{}-={}'.format(cor['amarelo'], cor['limpa'])*15)
t1= int(input('Primeiro termo: '))
r = int(input('Razão: '))
dt = t1 + (10 - 1) * r # decimo termo 
for i in range(t1, dt + r, r):
    print('{} -> '.format(i), end=' ')
print('ACABOU')