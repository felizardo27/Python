print('====== EX 013 ======')
print('Faça um algoritmo que leia o sálario de um funcionario e mostre seu novo sálario, com 15% de aumento')
sal = float(input('Digite o sálario R$'))
nsal = sal + (sal * 15/100)
print ('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, nsal))