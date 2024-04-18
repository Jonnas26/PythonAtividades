num1 = int(input('Digite um numero :'))
num2 = int(input('Digite outro numero :'))
#Comparando se o 1º numero é maior ou menor que o 2º numero#
maior = menor = num1
if num2 > num1:
    maior = num2
if num2 < num1:
    menor = num2
print(f'O maior numero digitado foi {maior}.\nO menor numero digitado foi {menor}.')
