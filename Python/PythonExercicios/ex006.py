print('====== EX 006 ======')
print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada')
n= int(input('Digite um número: '))
print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} vale {:.2f}.'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))
