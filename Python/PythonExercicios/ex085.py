# Exercício Python 085:
# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
nums = [[], []]
num = 0
for n in range(1, 8):
    num = int(input(f'Digite {n}º número: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
nums[0].sort()
nums[1].sort()
print('-' * 30)
print(f'Os números pares são {nums[0]}')
print(f'Os números ímpares são {nums[1]}')