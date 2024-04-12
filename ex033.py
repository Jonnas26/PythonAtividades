num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))
num3 = int(input('Digite o ultimo numero:'))
# Achando o maior e menor dos 3 numeros #
maior = num1
menor = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'O maior numero foi {maior} .')
print(f'O menor numero foi {menor} .')
