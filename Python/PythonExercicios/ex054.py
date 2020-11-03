# Exercício Python 54: Crie um programa que leia
# o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
print('\033[1;33m====== EX 054 ======\033[m')
import datetime
cont_maior = 0
cont_menor = 0
ano_atual = datetime.date.today().year
for p in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(p)))
    idade = ano_atual - nasc
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont_maior))
print('E também tivemos {} pessoas menores de idade'.format(cont_menor))
