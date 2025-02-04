from time import sleep

def linha():
    print('--' * 20)


def contagem(i, f , p):
    linha()
    print(f'Contando de {i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contagem(1,10,1)
contagem(10,1,1)
linha()
print('Agora é sua vez de personalizar a contagem !')
inicio = int(input('Inicio : '))
fim = int(input('Fim : '))
passo = int(input('Passo : '))
contagem(inicio, fim, passo)
