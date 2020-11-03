print('====== EX 017 ======')
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.
# (x, y)sqrt(x*x + y*y)
from math import hypot
x = float(input('Comprimento do Cateto oposto: '))
y = float(input('Comprimento do Cateto adjacente: '))
hip = hypot(x, y)
print('A hipotenusa vai medir {:.2f}'.format(hip))

'''======modo sem modulo====='''
# x = float(input('Comprimento do Cateto oposto: '))
# y = float(input('Comprimento do Cateto adjacente: '))
# hip = ((x ** 2) + (y ** 2)) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hip))
