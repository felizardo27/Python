print('====== EX 029 ======')
v = float(input('\033[1;36mQual a velocidade do carro?\033[m '))
if v > 80:
    print('\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[m')
    multa = (v - 80) * 7
    print('\033[1;31mVocê deve pagar uma multa de R${:.2f}\033[m'.format(multa))
print('\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')
