def resumo( num, a , b, formato=False):
    titulo('CALCULANDO OS VALORES')
    lista = [("valor a ser analisado:" ,moeda(num)),
             ("O Dobro a do valor:" , moeda(dobro(num)),),
             ("A metade do valor:" , moeda(metade(num))),
             (f"Com um aumento de {a}%:" , moeda(num + (num * a/100))),
             (f'Com uma redução de {b}%:' , moeda(num - (num * b/100)))]
    for l in range(len(lista)):
        if l % 2 == 0:
            print(f'{lista[l][0]:<30} {lista[l][1]:^20}')
        else:
            print(f'{lista[l][0]:<30} {lista[l][1]:^20}')


def metade(num=0 , formato=False):
    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num=0 , formato=False):
    res = num * 2
    return res if formato is False else moeda(res)


def reducao(num=0 , b=0, formato=False):
    res = num - (num * b/100)
    return res if formato is False else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')


def titulo(msg):
    tamanho = len(msg) + 30
    print('=' * tamanho)
    print(f'    {msg:^40}')
    print('=' * tamanho)

