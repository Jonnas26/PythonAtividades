a = int(input('Digite um numero:'))
b = int(input('Digite um numero:'))
c = int(input('Digite um numero:'))
#CALCULO PARA SABER SE DAR DE FORMAR UM TRIANGULO#
if a + b > c and b + c > a and c + a > b:
    #DESCOBRINDO O TIPO DE TRIANGULO#
    if a == b == c:
        print('É UM TRIANGULO EQUILATERO!Da de formar um triangulo.\n"TODOS LADOS IGUAIS"')
    elif a != b != c != a:
        print('É UM TRIANGULO ESCALENO!\n"TODOS LADOS DIFERENTES"')
    else:
        print('É UM TRIANGULO  ISÒCELES!\n"DOIS LADOS IGUAIS')
else:
    print('Não da de formar um triangulo.')
