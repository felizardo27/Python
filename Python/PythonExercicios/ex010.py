print('====== EX 010 ======')
print('Crie um programa em que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar\nConsiderando US$1,00 = R$3,27')
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você consegue comprar US${:.2f} Dólares'.format(real, dolar))
