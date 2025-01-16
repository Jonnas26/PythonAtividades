from random import randint


def listanum(lista):
    for cont in range(0,5):
        lista.append(randint(1,10))
    print(f'Os 5 valores da lista foram :',end=' ')
    for n in lista:
        print(n,end=' ')
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'E a soma dos valores pares {lista}, é {soma}.')

numeros = []
listanum(numeros)
somapar(numeros)
