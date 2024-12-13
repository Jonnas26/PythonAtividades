numeros = [[],[],[]]
for n1 in range(0,3):
    n1 = int(input('Digite um numero: '))
    numeros[0].append(n1)
for n2 in range(0,3):
    n2 = int(input('Digite mais 3 numeros: '))
    numeros[1].append(n2)
for n3 in range(0,3):
    n3 = int(input('Digite mais 3 numeros novamente: '))
    numeros[2].append(n3)
print(numeros)
print('==' * 15)
for p1 in range(0,3):
    print(f'[{numeros[0][p1]:^5}]',end=' ')
print()
for p2 in range(0,3):
    print(f'[{numeros[1][p2]:^5}]',end=' ')
print()
for p3 in range(0,3):
    print(f'[{numeros[2][p3]:^5}]',end=' ')
