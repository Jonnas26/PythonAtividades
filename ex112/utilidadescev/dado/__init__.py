def leiaDinheiro(msg):
    valido = False
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: {entrada} é um preço invalido.')
        else:
            valido = True
            return float(entrada)