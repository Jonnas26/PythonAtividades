#PROGRESSÂO ARITMÉTICA COM WHILE#
primt = int(input('Qual o primeiro termo:'))
razao = int(input('Qual a razão:'))
termo = primt
cont = 0
while cont < 10:
    print(f'{termo} >' ,end='')
    termo += razao
    cont += 1
print('FIM')
