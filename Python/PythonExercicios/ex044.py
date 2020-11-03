# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('\033[1;33m====== EX 044 ======\033[m')
# print('{:=^40}'.format("LOJINHA\033[m")) - forma mostrada na aula
print(f'\033[1;33m{" LOJINHA ":=^40}\033[m')
prec = float(input('\033[1;33mPreço das compas: R$\033[m'))
print ('''\033[1;34mForma de pagamento:
[ 1 ] - à vista em DINHEIRO 
[ 2 ] - à vista no CARTÃO
[ 3 ] - 2x no CARTÃO
[ 4 ] - 3x ou mais no CARTÃO\033[m''')
op = int(input('\033[1;33mDigite a opção desejada:\033[m '))
if op == 1:
    print('\033[1;36mÀ VISTA NO DINHEIRO - 10% DE DESCONTO\033[m')
    nprec = prec - ((10/100) * prec)
    print('\033[1;32mO valor do produto R${:.2f} com DESCONTO de 20% fica R${:.2f}\033[m'.format(prec, nprec))
elif op == 2:
    print('\033[1;36mÀ VISTA NO CARTÃO - 5% DE DESCONTO\033[m')
    nprec = prec - ((5 / 100) * prec)
    print('\033[1;32mO valor do produto R${:.2f} com DESCONTO de 5% fica R${:.2f}\033[m'.format(prec, nprec))
elif op == 3:
    print('\033[1;36mEm 2X no cartão - SEM JUROS\033[m')
    nprec = prec / 2
    print('\033[1;32mO valor do produto R${:.2f} em 2x fica R${:.2f}\033[m'.format(prec, nprec))
elif op == 4:
    par = int(input('\033[1;34mQuantas parcelas?\033[m '))
    print('\033[1;36mEm 3x no cartão ou mais - 20% de juros\033[m')
    nprec = (prec + ((20 / 100) * prec))
    nparc = nprec / par
    print('\033[1;32mSua compra será parcelada em {}x de R${:.2f} COM JUROS\033[m'.format(par, nparc))
    print('\033[1;32mSua compra de R${:.2f} vai custar R${:.2f} no final.\033[m'.format(prec, nprec))
else:
    print('\033[1;31mOPÇÃO INVALIDA!!\033[m')
