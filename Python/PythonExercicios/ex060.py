# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
print('\033[1;33m====== EX 060 ======\033[m')
# print('Digite um número para')
# n = int(input('Calcular o seu Fatorial: '))
# fat = 1
# print('Calculando {}! = '.format(n), end='')
# while n != 0:
#     print('{}'.format(n), end='')
#     print(' x ' if n > 1 else ' = ', end='')
#     fat *= n
#     n -= 1
# print('{}'.format(fat))

from math import factorial
print('Digite um número para')
n = int(input('Calcular o seu Fatorial: '))
f = n
fat = factorial(n)
print('Calculando {}! = '.format(n), end='')
while n != 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
print('{}'.format(fat))
print('O fatorial de {} é {}.'.format(f, fat))