# Exercício Python 090:
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
