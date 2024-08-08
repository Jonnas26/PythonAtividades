maior = menor = 0
#criando um laço para saber os valores
for c in range(0,5):
    peso = str(input(f'Quanto pesa a {c+1} pessoa:'))
#o primeiro peso a ser digitado é o maior e o menor por ser o primeiro e unico 
    if c == 0:
        maior = peso
        menor = peso
#apartir dos proximos a serem digitados é feita a seleção do MAIOR e o MENOR
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
#resultado
print(f'O maior peso foi de {maior}kgs.')
print(f'O menor peso foi de {menor}kgs.')
