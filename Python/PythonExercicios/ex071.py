# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('\033[1;33m====== EX 071 ======\033[m')
print(40*'-')
print('{:-^40}'.format(' BANCO PYTHON '))
print(40*'-')
saq = float(input('Qual o valor que você quer sacar? R$'))
total = saq
nota = 50
totalnot = 0
while True:
    if total >= nota:
        total -= nota
        totalnot += 1
    else:
        if totalnot > 0:
            print(f'Total de {totalnot} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnot = 0
        if total == 0:
            break
print(40*'-')
print('Volte sempre, até mais!')