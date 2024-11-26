print('--' * 20)
print('CALCULADOR DE MEDIA')
print('--' * 20)
maior = menor = cont = soma = 0
continuar = 'Ss'
while continuar in 'Ss':
    num = int(input('Digite um numero :'))
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('--' * 20)
print(f'Foram digitados {cont} numeros e a media deles é de {media:.2f}.')
print(f'O maior numero digitado foi {maior} e o menor {menor}.')
