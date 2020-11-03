# Exercício Python 56: Desenvolva um programa
# que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
print('\033[1;33m====== EX 056 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
soma_id = 0
cont = 0
media_id = 0
maior_id= 0
nome_maior= ''
contf20 = 0
for p in range(1, 5):
    print('{}-----{}ª PESSOA-----{}'.format(cor['ciano'],p, cor['limpa']))
    nome  = str(input('{}Nome:{} '.format(cor['verde'], cor['limpa']))).strip()
    idade = int(input('{}Idade:{} '.format(cor['verde'], cor['limpa'])))
    sexo = str(input('{}Sexo [M/F]:{} '.format(cor['verde'], cor['limpa']))).strip()
    soma_id += idade
    cont += 1
    if  p == 1 and sexo in 'Mm':
        maior_id = idade
        nome_maior = nome
    elif sexo in 'Mm' and idade > maior_id:
        maior_id = idade
        nome_maior = nome
    elif sexo in 'Mm'and idade < 20:
        contf20 += 1
media_id = soma_id / cont
print('A média de idade do grupo é de {} anos.'.format(media_id))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_id, nome_maior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contf20))