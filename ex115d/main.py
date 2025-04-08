from funções import*
from arquivo import*

arq = 'ListaDeCadastros.txt'

if not abrirArquivo(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['VER CADASTRADOS','CADASTRAR','SAIR'])
    if resposta == 1 :
        lerArquivo(arq)
    elif resposta == 2:
        nome = str(input('Nome : '))
        idade = leiaInt('Idade : ')
        cadastrarNovo(arq, nome, idade)
    elif resposta == 3:
        print('Até a proxima...')
        break
    else:
        print('DIGITE UMA OPÇÂO VALIDA!')
