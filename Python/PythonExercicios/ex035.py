print('====== EX 035 ======')
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {}, {}, {} podem formar um triângulo!'.format(r1, r2, r3))
else:
    print('As retas {}, {}, {} NÃO podem formar um triângulo!'.format(r1, r2, r3))