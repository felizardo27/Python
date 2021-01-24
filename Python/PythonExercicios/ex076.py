# Exercício Python 076:
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('\033[1;33m====== EX 076 ======\033[m')
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-='*20)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-='*20)
for p in range(0, len(listagem)):
    if p % 2 == 0:
        print(f'{listagem[p]:_<30}', end='')
    else:
        print(f'R$ {listagem[p]:0>5.2f}')
print('-='*20)
