# Exercício Python 079:
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
print('\033[1;33m====== EX 079 ======\033[m')
lista = []
while True:
    n = int(input('Digite um valor para a lista: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('ERROR!! valor ja cadastrado!')
    op = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if 'N' in op:
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
