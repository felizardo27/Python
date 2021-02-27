# Exercício Python 107:
# Crie um módulo chamado moeda.py
# que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
def aumentar(preco=0, taxa=0):
    am = preco + (preco * (taxa/100))
    return am

def diminuir(preco=0, taxa=0):
    dm = preco - (preco * (taxa/100))
    return dm


def dobro(preco=0):
    db = preco * 2
    return db


def metade(preco=0):
    mt = preco / 2
    return mt


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')