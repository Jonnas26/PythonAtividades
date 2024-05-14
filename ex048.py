#Fazendo a soma e contando todos os numeros impares entre 1 e 500#
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print(c,end=' -> ')
        cont += 1
        soma = soma + c
print('FIM')
print(f'No total entre 1 e 500 há {cont} numeros impares.')
print(f'E soma de todos eles é de {soma}')
