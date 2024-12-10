lista = []
par = []
impar = []
while True:
    n = int(input('Digite um numero :'))
    lista.append(n)
    while True:
        parar = str(input('Deseja parar ou continuar :')).strip().upper()[0]
        if parar in 'SN':
            break
        print('DIGITE SIM OU NÂO!')
    if parar in 'S':
        break
for i,v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Todos os numeros digitados foram {lista} .')
print(f'Os numeros pares foram {par}.')
print(f'Os numeros impares foram {impar}.')
