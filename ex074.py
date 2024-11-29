##maior e menor dentro de uma tupla
from random import randint
maior = menor = 0
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(numeros)
for n in range(0,len(numeros)):
    if n == 0:
        maior = numeros[n]
        menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        elif numeros[n] < menor:
            menor = numeros[n]
print(f'O maior numero foi {maior} .')
print(f'O menor numero foi {menor} .')
