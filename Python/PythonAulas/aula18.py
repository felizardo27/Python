# dados = list()
# dados.append('Cleiton') - adicionar item
# dados.append('21')

# pessoas = list()
# pessoas.append(dados[:]) - fazendo uma copia da lista dados
# teste = list()
# teste.append('João')
# teste.append(21)
# galera = list()
# galera.append(teste[:]) # copiando toda a lista
# teste[0] = 'Pedro'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# ou

# galera = [['João', 19], ['Pedro', 21], ['Ana', 24], ['Maria', 23]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

# ou

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
