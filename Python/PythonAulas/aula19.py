# Dicionários
# dados = dict()
# ou
# dados = {}
# dados = {'nome':'Pedro', 'idade':25}
# print(dados[nome])
# dados['sexo'] = 'M' - adicionar novo elemento
# del dados['idade'] - eliminar elemento
# filme = {'titulo':'Star Wars',
# 'ano':1977,
# 'diretor':'George Lucas'}
# print(filme.values()) - retornar todos os valores, ex = Star Wars
# print(filme.keys()) - retornar as chaves, ex - titulo
# print(filme.items()) - retornar tudo
# for k, v in filme.items():
#   print(f'0{k} é {v}')
# - O titulo é Star Wars
# - O ano é 1977
# - O diretor é George Lucas
#
# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 21}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# pessoas['nome'] = 'Cleiton' # alterando elemento
# pessoas['peso'] = 78.4 # adicionando elemento
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#
# brasil = list()
# estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
# estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])
#
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
