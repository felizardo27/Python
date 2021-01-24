# Exercício Python 080:
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
print('\033[1;33m====== EX 080 ======\033[m')
lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado na última posição')
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na {pos} posição')
                break
            pos += 1
print('=-'*30)
print(f'A lista digitada em ordem é {lista}')