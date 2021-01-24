# lista.append(' ') adiciona um elemento na lista
# lista.insert(0,' ') insere um elemento na lista na posição 0
#
# metodos para eliminar elementos em uma lista:
# del lanche[3] =  remove pela posição
# lanche.pop(3) = normalmente usado para eliminar o ultimo elemento - lanche.pop() - remove o ultimo elemento
# lanche.remove(' ') = remove pelo nome ou conteudo do elemento
#
# valores = list(range(4, 11)) = valores = [4, 5, 6, 7, 8, 9, 10]
# valores.sort() - ordenar todos os valores
# valores.sort(reverse=True) - ordenar os valores na ordem reversa
# len(valores) - contar quantos elementos tem na lista

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
# num.remove(2) # remove o primeiro elemento que achar
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

print('-'*40)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

print('-'*40)

a = [2, 3, 4, 7]
# b = a
# b[2] = 8 # altera o valor das duas listas pois tem uma ligação entre as duas
b = a[:] # cria uma copia de a em b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
