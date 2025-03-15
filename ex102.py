def fatorial(n, show=False):
    """CAlCULO DE FATORIAL

    :param n: O valor a ser calculado o fatorial
    :param show: (opcional) retorna ou não o calculo
    :return: O valor do FATORIAL do numero N
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c,end=' ')
            if c > 1:
                print(' x ' ,end='')
            else:
                print(' = ' ,end='')
        f *= c
    return f


print(fatorial(5, show=True))
#help(fatorial)
