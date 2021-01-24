# Exercício Python 082:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
print('\033[1;33m====== EX 082 ======\033[m')
lista = list()
listapar = list()
listaimpar = list()
while True:
    n = lista.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    if 'N' in op:
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'A lista completa é {lista}')
print(f'A lista dos pares é {listapar}')
print(f'A lista dos ímpares é {listaimpar}')