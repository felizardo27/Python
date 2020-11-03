nome = str(input('Qual o seu nome? '))
if nome == 'felizardo':
    print('Que nome top')
elif nome == 'João' or nome == 'Ana' or nome == 'Valentina' or nome == 'Enzo':
    print('Seu nome é muito simples')
elif nome in 'Paola Beatriz Tais':
    print('Belo nome feminino')
else:
    print('Seu nome não é top')
print('Tenha uma bom dia {}'.format(nome))