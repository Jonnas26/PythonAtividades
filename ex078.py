#Trabalhando com buscas e posições dentro de uma lista
numeros = []
maiornum = menornum = 0
for n in range(0,5):
    numeros.append(int(input(f'Digite o {n + 1}° numero :')))
    if n == 0:
        maiornum = menornum = numeros[n]
    else:
        if numeros[n] > maiornum:
            maiornum = numeros[n]
        elif numeros[n] < menornum:
            menornum = numeros[n]
print(numeros)
print(f'O maior numero digitado foi {maiornum} na posição ',end='')
for i,v in enumerate(numeros):
    if v == maiornum:
        print(f'{i + 1}...',end='')
print()
print(f'O menor numero digitado foi {menornum} na posição ',end='')
for i,v in enumerate(numeros):
    if v == menornum:
        print(f'{i + 1}...',end='')
