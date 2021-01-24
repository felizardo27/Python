# Exercício Python 095:
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
dados = dict()
time = list()
gols = list()
while True:
    gols.clear()
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    par = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for i in range(0, par):
        gols.append(int(input(f'  Quantos gols na partida {i+1}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
        else:
            print('ERROR! Coloque S ou N.')
    if op == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERROR! Jogador não existe!')
    else:
        print(f' --  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')
