##buscando por vogais dentro de uma TUPLA
palavras = ('ALEATORIA','CHIMARRAO','CASA','PREDIO','SURRA','PRISMATICO','LEGENDA')
for palavra in palavras:
    print(f'A palavra {palavra} tem as vogais ',end='')
    for vogal in palavra:
        if vogal in 'AEIOU':
            print(vogal,end=' ')
    print()
