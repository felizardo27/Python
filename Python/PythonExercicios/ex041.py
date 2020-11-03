# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
print('\033[1;33m====== EX 041 ======\033[m')
from datetime import date
nasc = str(input('Qual a sua data de nascimento? '))
dia = int(nasc[:2])
mes = int(nasc[3:5])
ano = int(nasc[6:])
ano_atual = date.today().year
id = ano_atual - ano
print('Sua idade é de {} anos'.format(id))
if id <= 9:
    print('Sua categoria é MIRIM!')
elif id <= 14:
    print('Sua categoria é INFANTIL!')
elif id <= 19:
    print('Sua categoria é JÚNIOR!')
elif id <= 25:
    print('Sua categoria é SÊNIOR!')
elif id > 25:
    print('Sua categoria é MASTER')