print('====== EX 004 ======')
n = input('Digite algo: ')
print('O tipo primitivo deste valor é {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('E alfabético? {}'.format(n.isalpha()))
print('É alfanumémrico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Ésta capitalizada? {}'.format(n.istitle()))
