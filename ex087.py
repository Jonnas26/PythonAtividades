soma = 0
maior = 0
numeros = [[],[],[]]
for n1 in range(0,3):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma += n1
    numeros[0].append(n1)
for n2 in range(0,3):
    n2 = int(input('Digite mais 3 numeros: '))
    if n2 % 2 == 0:
        soma += n2
    numeros[1].append(n2)
for n3 in range(0,3):
    n3 = int(input('Digite mais 3 numeros novamente: '))
    if n3 % 2 == 0:
        soma += n3
    numeros[2].append(n3)
print(numeros)
print('==' * 12)
for p1 in range(0,3):
    print(f'[{numeros[0][p1]:^5}]',end=' ')
print()
for p2 in range(0,3):
    print(f'[{numeros[1][p2]:^5}]',end=' ')
print()
for p3 in range(0,3):
    print(f'[{numeros[2][p3]:^5}]',end=' ')
print()
print('==' * 12)
print(f'A soma de todos os numeros pares foi de {soma} ao total.')
print(f'A soma de todos os numneros na terceira fileira é de {numeros[0][2] + numeros[1][2] + numeros[2][2]} ao total')
for segL in numeros[1]:
    print(segL)
    if segL > maior:
        maior = segL
    else:
        if segL > maior:
            maior = segL
print(f'O maior valor da segunda linha foi {maior}.')
