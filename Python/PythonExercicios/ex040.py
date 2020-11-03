# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
print('\033[1;33m====== EX 040 ======\033[m')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
md = (n1 + n2) / 2
if md >= 7.0:
    print('Sua média foi {:.1f}. Parabéns você está aprovado!'.format(md))
elif 7 > md >= 5:
    print('Sua média foi {:.1f}. Você está de Recuperação!'.format(md))
elif md < 5.0:
    print('Sua média foi {:.1f}. Reprovado, Se esforce mais!'.format(md))
