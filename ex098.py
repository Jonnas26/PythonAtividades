def contagem(i, f , p):
    print(f'Contando de {i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
        print('FIM!')
contagem(1,10,1)
contagem(10,1,1)