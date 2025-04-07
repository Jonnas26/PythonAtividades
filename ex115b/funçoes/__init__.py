c = ('\033[33m'  ,# 0 -> amarelo
     '\033[34m' ,# 1 -> azul
     '\033[m' ,   # 2 -> sem cor
    '\033[31m'  # 3 -> vermelho
     )


def linha():
    print('-' *30)


def titulo():
    print('-' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print(f'{c[0]}1 -{c[2]} {c[1]}VER PESSOAS CADASTRADAS\n{c[0]}2 -{c[2]} {c[1]}CADASTRAR NOVA PESSOA\n{c[0]}3 -{c[2]} {c[1]}SAIR DO SISTEMA{c[2]}')
    print('-' * 30)


def escolhaV(msg):
    from time import sleep
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{c[3]}ERRO: digite um numero inteiro valido{c[2]}')
            continue

        if n <1 or n >= 4:
            print(f'{c[3]}ERRO: digite uma opção valida (1 / 2 / 3).{c[2]}')
            sleep(2)
            titulo()
            continue
        return n


def arquivoExiste(nome):
    try:
        a = open('curso.txt','rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True