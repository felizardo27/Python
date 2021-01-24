# Exercício Python 081:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
print('\033[1;33m====== EX 081 ======\033[m')
lista = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    if 'N' in op:
        break
print(f'Foi digitado {len(lista)} números')
lista.sort(reverse=True)
print(f'A ordem decrescente da lista é {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi digitado!')
