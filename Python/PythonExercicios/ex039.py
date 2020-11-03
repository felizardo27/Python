#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
#  do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print('\033[1;33m====== EX 039 ======\033[m')
from datetime import date
nasc = str(input('Qual sua data de nascimento? ')).strip()
dia = int(nasc[:2])
mes = int(nasc[3:5])
ano = int(nasc[6:])
ano_atual = date.today().year
id = ano_atual - ano
print('Quem nasceu completa {} tem {} anos em {}.'.format(ano, id, ano_atual))
if id == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif id < 18:
    print('Ainda faltam {} anos para o alistamento\nSeu alistamento será em {}.'.format(18 - id, ano_atual + (18 - id)))
else:
    print('Você ja passou {} anos do prazo para se alistar.\nSeu alistamento foi em {}.'.format(id - 18, ano_atual - (id - 18)))
