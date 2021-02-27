# Exercício Python 107:
# Crie um módulo chamado moeda.py
# que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
def aumentar(preco=0, taxa=0, formato=False):
    am = preco + (preco * (taxa/100))
    return am if formato is False else moeda(am)

def diminuir(preco=0, taxa=0, formato=False):
    dm = preco - (preco * (taxa/100))
    return dm if formato is False else moeda(dm)


def dobro(preco=0, formato=False):
    db = preco * 2
    return db if formato is False else moeda(db)


def metade(preco=0, formato=True):
    mt = preco / 2
    return mt if formato is False else moeda(mt)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
