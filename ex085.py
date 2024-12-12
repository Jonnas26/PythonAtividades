numeros = [[],[]]
for n in range(0,7):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print(f'Numeros Pares : {numeros[0]}')
print(f'Numeros Impares : {numeros[1]}')
