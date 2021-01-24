# Exercício Python 074:
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
print('\033[1;33m====== EX 074 ======\033[m')
import random
lista = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10),)
print('Os número aleatórios são: ', end='')
for n in lista:
    print(f'{n} ', end='')
print(f'\nO maior valor foi: {max(lista)}')
print(f'O menor valor foi: {min(lista)}')