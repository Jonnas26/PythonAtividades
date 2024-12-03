#Trabalhando com buscas e posições dentro de uma lista
numeros = []
for n in range(0,5):
    numeros.append(int(input(f'Digite o {n + 1}° numero :')))
print(numeros)
maiornum = menornum = numeros[0]
for numero in numeros:
    if numero > maiornum:
        maiornum = numero
    elif numero < menornum:
        menornum = numero
print(f'O maior numero digitado foi {maiornum} na posição {numeros.index(maiornum) + 1}.')
print(f'O menor numero digitado foi {menornum} na posição {numeros.index(menornum) + 1}.')
