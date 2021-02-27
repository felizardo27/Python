# interactive help:
# help() - uma função interna de ajuda interativa
# help(print())
# print(input.__doc__)
# help(input)
#
# DOCSTRINGS
# Return
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)
# print(f'Os resultados foram {r1}, {r2} e {r3}.')
# pratica:
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
#
# # n = int(input('Difire um número: '))
# # print(f'O fatoral de {n} é igual a {fatorial(n)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}.')
#
#------------------------------------------------------------
#
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
# print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é par!')
