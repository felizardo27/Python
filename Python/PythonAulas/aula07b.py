print('\n===== DESAFIO 005 ====\n')
print('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.')
n = int(input('Digite um número: '))
print('O sucessor de {} é {} \ne o antecessor de {} é {}'.format(n, n+1, n, n-1))

print('\n===== DESAFIO 006 ====\n')
print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada')
n= int(input('Digite um número: '))
print('O seu dobro é igual a {}, o triplo igual a {} e sua raiz quadrada igual a {}'.format(n+n, n+n+n, n**(1/2)))

print('\n===== DESAFIO 007 ====\n')
print('Desenvolva um algoritmo que leia as duas notas de um aluno e calcule a sau média')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print('A sua média é {:.2f}'.format(media))

print('\n===== DESAFIO 008 ====\n')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros')
# decímetro: 10 decímetros correspondem a 1 metro.
# centímetro: 100 centímetros corresponde a 1 metro.
# milímetro: 1000 milímetros corresponde a 1 metro.
v = int(input('Digite um valor em metros: '))
print('{} m metros em centimetros é igual a {:0<2} cm e em milimetros é {:0<3} mn'.format(v, v, v))

print('\n===== DESAFIO 009 ====\n')
print('Faça um programa que leia um número inteiro e mostre na tela sua tabuada')
n = int(input('Digite um número: '))
print('{} * 1 = {}'.format(n, n*1))
print('{} * 2 = {}'.format(n, n*2))
print('{} * 3 = {}'.format(n, n*3))
print('{} * 4 = {}'.format(n, n*4))
print('{} * 5 = {}'.format(n, n*5))
print('{} * 6 = {}'.format(n, n*6))
print('{} * 7 = {}'.format(n, n*7))
print('{} * 8 = {}'.format(n, n*8))
print('{} * 9 = {}'.format(n, n*9))
print('{} * 10 = {}'.format(n, n*10))

print('\n===== DESAFIO 010 ====\n')
print('Crie um programa em que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar\nConsiderando US$1,00 = R$3,27')
dol = float(input('Digite quantos reais você possui na carteira: '))
print('Você consegue comprar US${} Dólares'.format(dol/3.27))

print('\n===== DESAFIO 011 ====\n')
print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade necessária para pinta-la\n'
      'sabendo que cada litro de tinta pinta uma area de 2m²')
lg = float(input('Largura: '))
al = float(input('Altura: '))
a = lg * al
c = a / 2
print('Em uma parede de {:.1f}m largura x {:.1f}m altura, sua área total é de {:.1f}m e seu consuo sera de {:.1f} litros de tinta'.format(lg, al, a, c))

print('\n===== DESAFIO 012 ====\n')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.')
pc = float(input('Digite o preço do produto sem deconto: '))
dc = pc * 0.05
dct = pc - dc
print('O valor do produto sem desconto é R${:.2f}\nE com o desconto de 5% é igual a R${:.2f}'.format(pc, dct))

print('\n===== DESAFIO 013 ====\n')
print('Faça um algoritmo que leia o sálario de um funcionario e mostre seu novo sálario, com 15% de aumento')
sal = float(input('Digite o sálario R$'))
aum = sal * 0.15
saln = sal + aum
print ('O o novo sálario com aumento de 15% é de R${}'.format(saln))
