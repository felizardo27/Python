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


def resumo(preco, au=0, di=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{au}% de aumento: \t{aumentar(preco,au, True)}')
    print(f'{di}% de redução: \t{diminuir(preco, di,True)}')
    print('-' * 30)
