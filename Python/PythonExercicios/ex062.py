# Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('\033[1;33m====== EX 062 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
print('{}-={}'.format(cor['amarelo'], cor['limpa'])*15)
print('GERADOR DE PA')
print('{}-={}'.format(cor['amarelo'], cor['limpa'])*15)
t1= int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = t1
cont = 1
total = 0
mais = 10
 # decimo termo
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(t), end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))