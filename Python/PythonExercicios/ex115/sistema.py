from lib.interface import *
from lib.arquivo import *
from time import sleep



arq = 'ex113.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    op = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if op == 1: #Listar pessoas
        lerArquivo(arq)
    elif op == 2: #Cadastrar pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif op == 3: #Sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERROR! Digite uma opção válida!\033[m')
    sleep(2)
