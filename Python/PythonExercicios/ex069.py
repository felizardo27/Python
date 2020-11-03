# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('\033[1;33m====== EX 069 ======\033[m')

maior = qde_h = qde_m = 0

while True:
    print('-'*25)
    print('   CADASTRE UMA PESSOA')
    print('-'*25)
    id = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)
    if id >= 18:
        maior += 1
    if sexo == 'M':
        qde_h += 1
    if sexo == 'F' and id < 20:
        qde_m += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {qde_h} homens cadastrados')
print(f'E temos {qde_m} mulheres com menos de 20 anos')
