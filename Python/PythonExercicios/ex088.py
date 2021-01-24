# Exercício Python 088:
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-'* 40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('-'* 40)
lista = list()
jogos = list()

op = int(input('Quantos jogos que sortear? '))
tot = 1
while tot <= op:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {op} JOGOS', '-=' *3)
for i, j in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {j}')
