# Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = dict()
dados['nome'] = str(input('Nome do Jogador: '))
par = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
gols = list()
for i in range(0, par):
    gols.append(int(input(f'  Quantos gols na partida {i}? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])}.')
for i, v in enumerate(dados["gols"]):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
