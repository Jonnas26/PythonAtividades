salario = float(input('Qual seu salario atual : R$ '))
#CALCULANDO UM SALARIO BASEANDO NO QUANTO QUE GANHA#
if salario >= 1250 :
    print(f'O seu novo salario será de R${((salario * 10) / 100)  + salario:.2f} (Aumento de 10% {((salario * 10) / 100):.2f})')
else:
    print(f'O seu novo salario será de R${((salario * 15) / 100) + salario:.2f} (Aumento de 15% {((salario * 15) / 100):.2f})')
