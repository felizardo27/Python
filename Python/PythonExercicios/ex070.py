# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('\033[1;33m====== EX 070 ======\033[m')
print(20*'-')
print('LOJA SUPER BARATÃO')
print(20*'-')
caro = menor = total = cont =0
barato = ''
while True:
    prod = str(input('Nome do Produto: ')).strip()
    prec = float(input('Preço: R$'))
    cont += 1
    total += prec
    if prec > 1000:
        caro += 1
    if cont == 1 or prec < menor:
        menor = prec
        barato = prod
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')
