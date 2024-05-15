#PROGRESSÂO ARITMÉTICA#
primt = int(input('Qual o primeiro termo:'))
razao = int(input('Qual a razão:'))
termo = primt + (11-1)*razao
for c in range(primt,termo,razao):
    print(f'{c} -> ',end="")
print('Acabou')
