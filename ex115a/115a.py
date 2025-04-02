from funçoes import titulo
from funçoes import escolhaV
from funçoes import linha


titulo()
while True:
    escolha = escolhaV('Qual sua escolha : ')
    if escolha == 3:
        linha()
        print(f'{"SAINDO DO SISTEMA...Até logo":^30}')
        linha()
        break
    else:
        linha()
        print(f'{"ESCOLHA " + str(escolha):^30}')
        linha()
