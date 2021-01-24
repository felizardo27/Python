# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
cadastros = list()
p = list()
mai = men = 0
while True:
    p.append(str(input('Nome: ')))
    p.append(float(input('Peso: ')))
    if len(cadastros) == 0:
        mai = men = p[1]
    else:
        if p[1] > mai:
            mai = p[1]
        elif p[1] < men:
            men = p[1]
    cadastros.append(p[:])
    p.clear()
    op = str(input('Cadastrar outra pessoa? [S/N] ')).upper().strip()
    if 'N' in op:
        break

print(f'Você cadastrou {len(cadastros)} pessoas.')
print(f'O maior peso é de {mai}kg. O maior peso de ', end='')
for p in cadastros:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'E o menor peso é de {men}kg. O menor peso de ', end='')
for p in cadastros:
    if p[1] == men:
        print(f'[{p[0]}] ', end='' )
print()
