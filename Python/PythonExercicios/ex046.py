# Exercício Python 46: Faça um programa que mostre na tela
# uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
print('\033[1;33m====== EX 046 ======\033[m')
cor = {'limpa':'\033[m',
        'vermelho':'\033[1;31m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1;32m',
        'branco':'\033[1;30m',
        'ciano':'\033[1;36m',
        'azul':'\033[1;34m'}
import pyglet
import time
def explosao():
        fogos = pyglet.image.load_animation('fogos46.gif')
        FogosGif = pyglet.sprite.Sprite(fogos)

        w = FogosGif.width
        h = FogosGif.height

        window = pyglet.window.Window(width=w, height=h)
        r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
        @window.event
        def on_draw():
                window.clear()
                FogosGif.draw()

        pyglet.app.run()

for cont in range(10, -1, -1):
        print('{}{:2}{}'.format(cor['ciano'], cont, cor['limpa']))
        time.sleep(0.5)
explosao()
