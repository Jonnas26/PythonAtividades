listanum = []
while True:
    numero = (int(input('Digite um numero :')))
    if numero in (listanum):
        print('Digite um numero que não foi digitado!')
    else:
        listanum.append(numero)
        while True:
            stop = str(input('Quer continuar :')).strip().upper()[0]
            if stop in 'SN':
                break
            print('DIGITE SIM OU NAO')
    if stop in 'N':
        break
listanum.sort()
print(listanum)
