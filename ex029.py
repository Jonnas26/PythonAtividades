velocidade = int(input('Quantos quilometros esta passando na via:'))
multa = (velocidade - 80) * 7
if velocidade >= 80:
    print(f'Você foi multado hein R${multa:.2f}.')
else:
    print('Tudo bem, esta no limite permitido abaixo dos 80 KM.')
