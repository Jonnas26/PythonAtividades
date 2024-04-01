from math import sqrt , ceil
catetopo = float(input('Qual o cateto oposto:'))
catetoad = float(input('Qual o cateto adjacente:'))
hipot = sqrt((catetopo ** 2 + catetoad ** 2)) 
print(f'Valor da hipotenusa = {hipot:.2f}')
