baratop = ' '
total = maior1k = barato = 0
print('--' * 20)
print('SUPERMERCADO')
print('--' * 20)
while True:
    nomeprod = str(input('Qual o nome do produto :')).strip().upper()
    precoprod = float(input('Qual o preço do produto:'))
    if precoprod > barato:
        barato = precoprod
        baratop = nomeprod
    elif barato > precoprod:
        barato = precoprod
        baratop = nomeprod
    if precoprod > 1000.00:
        maior1k += 1
    total += precoprod
    cont = str(input('Vai passar mais algum produto? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print('___' * 20)
print(f'O total de gastos dessa compra foi de R${total:.2f} .')
print(f'Teve {maior1k} produtos com preços superior a mil reais.')
print(f'O produto mais barato da compra foi {baratop} .')
