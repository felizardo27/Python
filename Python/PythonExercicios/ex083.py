# Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
print('\033[1;33m====== EX 083 ======\033[m')
expr = str(input('Digite uma expressão: '))
pilha = list()
for i in expr:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão está correta')
else:
    print('A expressão está incorreta')

