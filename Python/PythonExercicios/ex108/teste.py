# Exercício Python 108:
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
import moeda


num = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(num)} é de R${moeda.moeda(moeda.metade(num))}')
print(f'O dobro de R${moeda.moeda(num)} é de R${moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(num, 10))}')