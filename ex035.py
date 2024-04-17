a = int(input('Digite um numero:'))
b = int(input('Digite um numero:'))
c = int(input('Digite um numero:'))
#CALCULO PARA SABER SE DAR DE FORMAR UM TRIANGULO#
if a + b > c and b + c > a and c + a > b:
    print('Da de formar um triangulo.')
else:
    print('Não da de formar um triangulo.')
