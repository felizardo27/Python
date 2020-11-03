# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('\033[1;33m====== EX 068 ======\033[m')
import random
print('-='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*25)
cont = 0
while True:
    j = int(input('Diga um valor: '))
    pc = random.randint(0, 11)
    total = j + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {j} e o computador {pc}. Total foi de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
                print('Você VENCEU!')
                cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            cont += 1
        else:
            print('VocÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
