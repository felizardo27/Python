print('====== EX 018 ======')
# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
import math
n = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(n, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(n, tan))
