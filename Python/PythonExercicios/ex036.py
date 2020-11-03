# Escreva um programa para aprovar o emprestimo bancario para o a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos vai pagar.
# Calcule o valor da pestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.
print('\033[1;33m====== EX 036 ======\033[m')
cor = {'limpa': '\033[m',
       'azul': '\033[1;34m',
       'amarelo': '\033[1;33m',
       'vermelho': '\033[1;31m',
       'verde': '\033[1;32m'}
casa = float(input('{}Qual o valor da casa?{} R$'.format(cor['azul'], cor['limpa'])))
sal = float(input('{}Qual o seu salário?{} R$'.format(cor['azul'], cor['limpa'])))
anos = int(input('{}Quantos anos você vai pagar a casa?{} '.format(cor['azul'], cor['limpa'])))
minimo = sal * 30 / 100
valmen = casa / (anos * 12)
print('{}Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}{}'.format(cor['azul'], casa, anos, valmen, cor['limpa']))
if valmen >= minimo:
    print('{}Empréstimo NEGADO!{}'.format(cor['vermelho'], cor['limpa']))
elif valmen <= minimo:
    print('{}Empréstimo CONCEDIDO!{}'.format(cor['verde'], cor['limpa']))
