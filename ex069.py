maior18 = toth = mulhern = 0
print('==' * 20)
print('ANALISE DE DADOS')
print('==' * 20)
while True:
    idade = int(input('Quantos anos tem?'))
    if idade >= 18:
        maior18 += 1
    sexo = ' '
    while sexo not in "FM":
        sexo = str(input('Qual o seu sexo? [F/M]')).strip().upper()[0]
        if sexo == 'M':
            toth += 1
        if sexo == 'F':
            if idade < 20:
                mulhern += 1
    cont = ' '
    while cont not in "SN":
        cont = str(input('Quer cadastrar mais uma pessoa? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print('--' * 20)
print(f'Teve o total de {maior18} pessoas com idades maior ou igual a 18.')
print(f'Foram cadastrados {toth} homens.')
print(f'Foi cadastrado um total de {mulhern} mulheres com idades inferiores a 20 anos.')
