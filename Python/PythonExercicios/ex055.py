# Exercício Python 55: Faça um programa
# que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
print('\033[1;33m====== EX 055 ======\033[m')
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso é de {}Kg\nO menor peso é de {}Kg'.format(maior, menor))