# Exercício Python 48: Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
print('\033[1;33m====== EX 048 ======\033[m')
soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        soma += x
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))