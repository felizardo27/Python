print('\n=====DESAFIO 16=====\n')
#Crie um programa que leia um número real qualquer pelo teclado
# e mostre a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
import math
n = float(input('Digite um número: '))
print('O número {} tem a a parte inteira {}.'.format(n, math.trunc(n)))

print('\n=====DESAFIO 17=====\n')
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.
# (x, y)sqrt(x*x + y*y)
x = int(input('Digite o Cateto oposto: '))
y = int(input('Digite o Cateto adjacente: '))
hip = math.hypot(x, y)
print('A hipotenusa de {} cateto oposto e de {} cateto adjacente é igual a {:.2f}'.format(x, y, hip))

import cmath
print('\n=====DESAFIO 18=====\n')
# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
# n = int(input('Digite o ângulo: '))
# print('O ângulo {}º, em cos = {}, seno = {}, tang = {}'.format(n, math.acos(n), math.asin(n), math.atan(n)))

print('\n=====DESAFIO 19=====\n')
import random
# Um professor quer sortear um dos seus quatro alunos para apagr o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# aluno1 = str(input('Digite o nome do aluno 1: '))
# aluno2 = str(input('Digite o nome do aluno 2: '))
# aluno3 = str(input('Digite o nome do aluno 3: '))
# aluno4 = str(input('Digite o nome do aluno 4: '))
# deck = 'aluno1, aluno2, aluno3, aluno4'.split()
# print(random.shuffle(deck))


print('\n=====DESAFIO 20=====\n')
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('\n=====DESAFIO 21=====\n')
# Faça um programa em python que abra e reproduza o audio de um arquivo MP3.
