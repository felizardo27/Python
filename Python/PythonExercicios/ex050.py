# Exercício Python 50: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
print('\033[1;33m====== EX 050 ======\033[m')
soma = 0
cont = 0
for x in range(1, 7):
    n = int(input('Digite o número {} : '.format(x)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} número PARES e a soma entre eles é de {}'.format(cont, soma))