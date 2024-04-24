produto = float(input('Qual o valor do produto:'))
print('ESCOLHA A FORMA DE PAGAMENTO:\n[0]A vista (dinheiro ou cheque)\n[1]A vista no cartão\n[2]2x no cartão\n[3]3x ou mais no cartão.')
escolha = int(input('ESCOLHA A FORMA DE PAGAMENTO - > '))
if escolha == 0:
    print(f'O Total a ser pago será de R${produto - ((produto*10)/100):.2f} -- 10% de desconto!')
elif escolha == 1:
    print(f'O total a ser pago será de R${produto - ((produto*5)/100):.2f} -- 5% de desconto!')
elif escolha == 2:
    print(f'O total a ser pago será de R${produto:.2f} -- Valor normal!')
elif escolha == 3:
    print(f'O total a ser pago será de R${produto + ((produto*20)/100):.2f} -- 20% a mais de juros!')
