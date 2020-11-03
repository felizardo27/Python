# Exercício Python 47: Crie um programa que
# mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('\033[1;33m====== EX 047 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
for count in range(2, 51, 2):
    print(count, end=' ')
print('Todos os número pares de 0 a 50')
