# Exercício Python 72:
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
print('\033[1;33m====== EX 072 ======\033[m')
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    pos = int(input('Digite um número de 0 a 20: '))
    if 0 <= pos <=20:
        print(f'Você digitou o número {numeros[pos]}')
        op = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if op in 'N':
            break
    else:
        print('Número inválido, tente novamente!')
