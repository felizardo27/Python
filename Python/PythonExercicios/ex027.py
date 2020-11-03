# Exercício Python 27:
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('====== EX 027 ======')
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome)-1])) ou
print('Seu último nome é {}'.format(nome[-1])) # -1 pega o ultimo valor, -2 penultimo, ... e assim por diante
