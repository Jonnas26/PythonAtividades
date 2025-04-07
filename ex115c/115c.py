from funçoes import *
from arquivo import *


arq = 'Curso.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criaArquivo(arq)


titulo()
while True:
    escolha = escolhaV('Qual sua escolha : ')
    if escolha == 1:
        lerArquivo(arq)
    elif escolha == 2:
        linha()
        print("[2] CADASTRAR NOVA PESSOA")
        linha()
        nome = str(input('NOME :'))
        idade = leiaInt('IDADE')
        cadastrarNovo(arq,nome,idade)
    elif escolha == 3:
        linha()
        print(f'{"SAINDO DO SISTEMA...Até logo":^30}')
        linha()
        break
