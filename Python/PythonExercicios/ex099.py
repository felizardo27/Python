# Exercício Python 099:
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* nums):
    print('-=' * 30)
    print('Analisando os valores passados...')
    cont = maior = 0
    for v in nums:
        print(f'{v} ', end='')
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor inforamdo foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
