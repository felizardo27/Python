# Exercício Python 73: Crie uma tupla preenchida
# com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
print('\033[1;33m====== EX 073 ======\033[m')
fut = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
       'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthias',
       'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
       'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
       'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'Lista dos times do Brasileirão: \n{fut} ')

print('-'*250)

print(f'Os 5 primeiros times: \n{fut[0:5]}')

print('-'*250)

print(f'Os 4 ultimos times: \n{fut[-4:]}')

print('-'*250)

print(f'Times em ordem alfabética: \n{sorted(fut)}')

print('-'*250)

print(f'A Chapecoense está na {fut.index("Chapecoense")+1}ª posição ')