maior = menor = 0
#criando o loop de perguntas sobre a idade
for c in range(0,7):
    idade = int(input(f'Quantos anos a {c+1}º pessoa tem?'))
#se o primeiro for "c" e a "idade" maior que "c" ele sera o maior e o menor
    if c == 0 and idade > c:
        maior = idade
        menor = idade
#sabendo se alguma idade depois do primeiro for maior será o maior ou menor será o menor
    elif c > maior:
        maior = idade
    elif c < menor:
        menor = idade
#resultado
print(f'Maior idade foi de {maior} anos,'
      f'A menor idade foi de {menor} anos')
