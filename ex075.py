numeros = (int(input('Digite um numero :')),
           int(input('Digite um numero:')),
           int(input('Digite um numero:')),
           int(input('Digite um numero :')))
print(numeros)
print(f'O numero 9 aparece um total de {numeros.count(9)} vezes .')
if 3 in numeros:
    print(f'O numero 3 foi digita na posição {numeros.index(3) + 1}')
else:print('O numero 3 não foi digitado .')
print('Os numeros pares digitados foram',end=' ')
for p in range(0,len(numeros)):
    if numeros[p] % 2 == 0:
        print(f'{numeros[p]}',end=' ')