cont = 0
soma = 0
num = int(input('Digite um numero [DIGITE 999 PARA PARAR] :'))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero [DIGITE 999 PARA PARAR] :'))
print(f'fora digitados {cont} numeros e a soma deles foi de {soma} no total.')
