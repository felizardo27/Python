# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('\033[1;33m====== EX 065 ======\033[m')

op = 'Ss'
cont = soma = media = maior = menor = 0
while op in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    op = str(input('Quer continuar? [S/N]')).strip().upper()
media = soma / cont
print('Você digitou {} números e a média foi de {}'.format(cont, media))
print('O maior númeoro foi {} e o menor {}'.format(maior, menor))
