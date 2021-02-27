def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mError \"{valor}\" é um preço inválido!\033[m')
        else:
            return float(valor)

