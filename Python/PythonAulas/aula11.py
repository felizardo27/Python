# padrao ansi
# exemplo *** \033[style;text;backm ***
# style - 0 = none; 1 = bold; 4 = underline; 7 = negative
# text - 30 = branco, 31 = vermelho; 32 = verde; 33 = amarelo; 34 = azul; 35 = magenta; 36 = ciano; 37 = cinza;
# para colocar mais usar uma biblioteca por fora
# back - 40 = branco, 41 = vermelho; 42 = verde; 43 = amarelo; 44 = azul; 45 = magenta; 46 = ciano; 47 = cinza;
# print('\033[7;30mOlá Mundo!\033[m')
# a = 3
# b = 5
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Felizardo'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))