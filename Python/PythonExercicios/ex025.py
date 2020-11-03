# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
print('====== EX 025 ======')
nome = str(input('Qual é o seu nome completo? ')).lower().split()
print('Seu nome tem Silva? {}'.format('silva' in nome))
 