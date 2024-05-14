#Soma e conta de apenas numeros pares#
cont = tot = 0
for c in range(0,6):
    num = int(input(f'Digite o {c+1}º numero:'))
    if num % 2 == 0:
        cont += 1
        tot += num
print(f'Foram digitados {cont} numeros pares.\nE a soma dels é igual a {tot}')
