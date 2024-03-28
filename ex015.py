km = int(input('Quantos KM rodou no carro:'))
tempo = int(input('Quantos dias ficou alugado:'))
taxa = (tempo * 60) + (km * 0.15)
print(f'O total a ser pago é de R${taxa}')
