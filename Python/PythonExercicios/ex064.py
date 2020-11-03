# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('\033[1;33m====== EX 064 ======\033[m')

n = 0
n_cont = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        n_cont += n
        cont += 1
print('Você digitou {} vezes e a soma de todos os valores é de {}'.format(cont, n_cont))