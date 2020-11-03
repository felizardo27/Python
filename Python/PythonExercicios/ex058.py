# Exercício Python 58: Melhore o jogo do DESAFIO 28
# onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
print('\033[1;33m====== EX 058 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
print('{}JOGO DE ADIVINHAÇÃO{}'.format(cor['branco'], cor['limpa']))
from random import randint #impotando função numero aleatorio do modulo random
computador = randint(0, 10)
print('{}-=-{}'.format(cor['amarelo'],cor['limpa']) * 20)
print('{}Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.. \nTente adivinhar qual foi{}'.format(cor['ciano'], cor['limpa']))
print('{}-=-{}'.format(cor['amarelo'],cor['limpa']) * 20)
acertou = False
score = 0
while not acertou:
    jogador = int(input('{}Qual o seu palpite?{} '.format(cor['branco'], cor['limpa'])))
    score += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('{}Mais.. Tente mais uma vez.{}'.format(cor['branco'], cor['limpa']))
        elif jogador > computador:
            print('{}Menos.. Tente mais uma vez.{}'.format(cor['branco'], cor['limpa']))
print('{}Acertou!! Com uma pontuação de {}.{}'.format(cor['verde'], score, cor['limpa']))
