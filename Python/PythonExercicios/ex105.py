# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
def notas(*nts, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    n = dict()
    n['Total'] = len(nts)
    n['Maior'] = max(nts)
    n['Menor'] = min(nts)
    n['Média'] = sum(nts) / len(nts)
    if sit:
        if n['Média'] >= 7:
            n['Situação'] = 'BOA'
        elif 5 <= n['Média'] < 7:
            n['Situação'] = 'RAZOÁVEL'
        elif n['Média'] < 5:
            n['Situação'] = 'RUIM'
    return n


resp = notas(5.5, 10, 5.5, sit=True)
print(resp)
# help(notas)
