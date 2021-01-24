# Exercício Python 075:
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
print('\033[1;33m====== EX 075 ======\033[m')

nums = (int(input('Digite um número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os números {nums}')
print(f'O número 9 apareceu {nums.count(9)} vezes')
if '3' in nums:
    print(f'O número 3 foi digitado primeiro na posição {nums.index(3)+1}')
else:
    print('Não foi encontrado número 3 na tupla')
print('Os números pares são: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')
