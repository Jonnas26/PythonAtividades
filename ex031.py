km = int(input('Quantos KM é a distancia da sua viagem?'))
if km <= 200:
    #Calculo da passagem é de 50 centavos por KM#
    print(f'O total da sua passagem será de R${km*0.50 :.2f}')
else:
    #Calculo da passagem é de 45 centavos por KM#
    print(f'O total da sua passagem será de R${km * 0.45:.2f}')
    