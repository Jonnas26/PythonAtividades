from funçoes import escolhaV
from funçoes import linha
from funçoes import titulo
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
    elif escolha == 3:
        linha()
        print(f'{"SAINDO DO SISTEMA...Até logo":^30}')
        linha()
        break
    else:
        linha()
        print(f'{"ESCOLHA " + str(escolha):^30}')
        linha()
