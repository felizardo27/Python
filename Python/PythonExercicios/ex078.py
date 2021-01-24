print('\033[1;33m====== EX 078 ======\033[m')
nums = list()
for n in range(0, 5):
    nums.append(int(input(f'Digite um valor para a posição {n}: ')))
print('=-'*40)
print(f'Você digitou os valores {nums}')
print(f'O maior valor digitado foi {max(nums)} nas posições: ', end='')
for i, n in enumerate(nums):
    if n == max(nums):
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(nums)} nas posições: ', end='')
for i, n in enumerate(nums):
    if n == min(nums):
        print(f'{i}...', end='')
print()