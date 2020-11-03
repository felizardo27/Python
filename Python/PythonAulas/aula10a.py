# nome = str(input('Qual é o seu nome? '))
# if nome == 'João':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é estranho')
# print('Bom dia, {}!'.format(nome))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = ((n1 + n2) / 2)
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa PARABENS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')
print('PARABÉNS!' if m>=6 else 'ESTUDE MAIS!') # condição simplificada