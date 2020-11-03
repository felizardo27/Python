# Exercício Python 52: Faça um programa
# que leia um número inteiro e diga se ele é ou não um número primo.
print('\033[1;33m====== EX 052 ======\033[m')
n = int(input('Digite um número: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[1;36m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n\033[1;32mO número {} foi divisível {} vezes\033[m'.format(n, tot))
if tot == 2:
    print('\033[1;32mE por isso ele é PRIMO!\033[m')
else:
    print('\033[1;32mE por isso ele não é PRIMO!\033[m')
