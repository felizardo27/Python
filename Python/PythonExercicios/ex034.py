print('====== EX 034 ======')
sal = float(input('Qual o seu sálario? R$'))
if sal > 1250:
    aum = sal + (sal * (10 / 100))
    print('O seu aumento é de R${:.2f}'.format(aum))
else:
    aum = sal + (sal * (15 / 100))
    print('O seu aumento é de R${:.2f}'.format(aum))