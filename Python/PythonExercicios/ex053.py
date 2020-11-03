# Exercício Python 53: Crie um programa que leia uma frase
# qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.
print('\033[1;33m====== EX 053 ======\033[m')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase: {}'.format(junto))
inverso = ''
inverso = junto[::-1] # solução com fatiamento do python
# for letra in range(len(junto) - 1, -1, -1): # Solução com for
#     inverso += junto[letra]
print('O inverdo de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
