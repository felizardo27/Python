# Exercício Python 113:
# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[1;31mERROR! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[1;31mERROR! Digite um número real válido.\033[m')
            continue
        else:
            return n

ni = leiaInt('Digite um valor Inteiro: ')
nf = leiaFloat('Digite um valor Real: ')
print(f'O valor digitado foi {ni}')
print(f'O valor inteiro digitado foi {ni} e o real foi {nf}')
