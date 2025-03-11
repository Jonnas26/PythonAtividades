c = ('\033[m',        # 0 -> sem cor
    '\033[0;30;41m',   # 1 -> cor vermelha
    '\033[0;30;42m',   # 2 -> cor verde
    '\033[0;30;43m',   # 3 -> cor amarelo
    '\033[0;30;44m',   # 4 -> cor azul
    '\033[0;30;45m',   # 5 -> cor roxo
    '\033[7;30m'      # 6 -> cor branca
    )


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor] ,end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0],end='')


def ajuda(msg):
    titulo('Buscando o resumo de  \'{msg}\'' , 4)
    help(f'  {msg}')


comando = ''
while True:
    titulo('Ajudando de busca PYHelper!', 2)
    comando = str(input('Qual função ou biblioteca deseja ver >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até breve !' , 5)
