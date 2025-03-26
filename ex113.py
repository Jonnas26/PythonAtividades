def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('Digite um numero inteiro VALIDO!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo USUARIO!')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Digite um numero real VALIDO!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida peluo USUARIO!')
            return 0
        else:
            return n


#Começo de atividade usando TRY e EXCEPT
n1 = leiaint('Digite um numero INTEIRO:')
n2 = leiafloat('Digite um numero REAL :')
print(f'Você digitou {n1} como numero INTEIRO.')
print(f'Você digitou {n2} como numero REAL.')
