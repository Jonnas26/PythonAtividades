def linha():
    print('--' * 20)


def numeros(* núm):
    maior = menor = núm[0]
    linha()
    print('Analisando os numeros passados...')
    print(f'{núm} Foram informados {len(núm)} numeros.')
    for m in núm:
        if m > maior:
            maior = m
        if m < menor:
            menor = m
    print(f'E o maior numero informado é {maior} e o menor é {menor}.')


numeros(1,3,6,7,8)
numeros(4,7,3,1)
numeros(4,2)
numeros(4,7,3,9,12,42)
