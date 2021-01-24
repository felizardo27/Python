lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis]
# lanche[1] = 'Refrigerant' ERRADO
print(lanche)

print('-'*40)

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-'*40)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')


print('-'*40)

for cont, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {cont}')

print('Comi muito!!')

print('-'*40)

print(sorted(lanche)) # organizar tupla em ordem

print('-'*40)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # Somando duas tuplas
print(c)
print(c.count(5)) # somar quantas vezes aparece tal número dentro da tupla
print(c.index(2)) # mostra posição do elemento na tupla, se tiver mais de um elemento pega na primeira ocorrencia
print(c.index(5, 1)) # buscando o elemento na tupla apartir do elemento 1, pulando o elemento 0, deslocamento

print('-'*40)

pessoa = ('Cleiton', 27, 'M', 73.45) # dentro das tuplas pode ter dados de tipos diferentes
#del(pessoa) # apagando a variavel
print(pessoa)
