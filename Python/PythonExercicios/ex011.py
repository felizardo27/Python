print('====== EX 011 ======')
print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade necessária para pinta-la\n'
      'sabendo que cada litro de tinta pinta uma area de 2m².\n')
lg = float(input('Largura: '))
al = float(input('Altura: '))
a = lg * al
c = a / 2
print('Sua parede tem dimensão de {}m x {}m e sua área total é de {}m².\nPara pintar essa parede, você precisará de {}L de tinta.'.format(lg, al, a, c))
