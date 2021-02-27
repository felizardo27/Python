# Exercício Python 107:
# Crie um módulo chamado moeda.py
# que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preco, taxa):
    am = preco + (preco * (taxa/100))
    return am

def diminuir(preco, taxa):
    dm = preco - (preco * (taxa/100))
    return dm


def dobro(preco):
    db = preco * 2
    return db

def metade(preco):
    mt = preco / 2
    return mt