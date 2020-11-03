print('====== EX 031 ======')
dist = int(input('Qual a distância da sua viagem? '))
# if dist <= 200:
#     pas = dist * 0.5
# elif dist > 200:
#     pas = dist * 0.45
# ou
pas = dist * 0.5 if dist <=200 else dist * 0.45 # if simplificado
print('O valor da sua passagem é de R${:.2f}'.format(pas))
print('Tenha uma boa viagem!')
