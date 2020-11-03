print('====== EX 028 ======')
cor = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'verde':'\033[1;32m',
         'branco':'\033[1;30m',
         'pretoebranco':'\033[7;30m'}
print('{}JOGO DE ADIVINHAÇÃO{}'.format(cor['branco'], cor['limpa']))
from random import randint #impotando função numero aleatorio do modulo random
from time import sleep # importando do modulo time, função sleep para deixar o computador "dormindo" por um tempo
computador = randint(0, 5)
print('{}-=-{}'.format(cor['amarelo'],cor['limpa']) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cor['vermelho'], cor['limpa']))
print('{}-=-{}'.format(cor['amarelo'],cor['limpa']) * 20)
jogador = int(input('{}Em que número eu pensei?{} '.format(cor['branco'], cor['limpa'])))
print('{}PROCESSANDO...{}'.format(cor['amarelo'], cor['limpa']))
sleep(3)
if jogador == computador:
    print('{}PARABÉNS!! Você conseguiu me vencer!{}'.format(cor['verde'], cor['limpa']))
else:
    print('{}GANHEI!! Eu pensei no número {} e não no {}{}'.format(cor['vermelho'], computador, jogador, cor['limpa']))
