# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
print('\033[1;33m====== EX 042 ======\033[m')
print('\033[1;33m-=\033[m'*20)
print('\033[1;31mAnalisador de Triângulos V2.0\033[m')
print('\033[1;33m-=\033[m'*20)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {}, {}, {} podem formar um triângulo!'.format(r1, r2, r3), end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('As retas {}, {}, {} NÃO podem formar um triângulo!'.format(r1, r2, r3))