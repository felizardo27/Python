# n = s = 0
# while True:
#     n = int((input('Digite um número: ')))
#     if n == 999:
#         break
#     s += n
# # print('A soma vale {}'.format(s))
# print(f'A soma vale {s}') # f strings

# nome = 'João'
# idade = 33
# print(f'O {nome} tem {idade} anos') # python 3.6+
# print('O {} tem {} anos'.format(nome, idade)) # python 3
# print('O %s tem %d anos' %(nome, idade)) # python2

nome = 'João'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
# {nome:20 # adicionar 20 espaços
# {nome:^20} # centralizar nome em 20 espaços
# {nome:-^20} # centraliar nome com '-' em 20 espaços
# {nome:-<20} # centraliar a esquerda nome com '-' em 20 espaços
# {nome:->20} # centraliar a direita nome com '-' em 20 espaços