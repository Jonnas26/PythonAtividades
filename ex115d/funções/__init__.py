def linha():
    print('-' * 30)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError,ValueError):
            print('ERRO : Digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('ERRO: usuario interrompeu a operação!')
            return 0
        return n
    

def cabeçalho(msg):
    linha()
    print(f'{msg:^30}')
    linha()
    

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    i = 1
    for c in lista:
        print(f'[{i}] {c}')
        i += 1
    linha()
    escolha = leiaInt('Qual sua escolha:')
    return escolha


