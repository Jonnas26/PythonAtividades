##usando tupla para montar uma tabela de preço e produto
produtos = ('ARROS','20,00','FEIJÂO','10,50',
            'FARINHA','05,67','CARNE','14,99',
            'F.MIGNON','50,00','TOMATE','02,50')
print(f'{'PRODUTO':=<33}{'PREÇO'}')
print('-' * 39)
for c in range(0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}' ,end='')
    elif c % 2 == 1:
        print(f'R$ {produtos[c]:.<5}.')
