lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    while True:
        parar = str(input('Deseja parar? [S/N]')).strip().upper()[0]
        if parar in 'SN':
            break
        print('DIGITE SIM OU NÂO')
    if parar in 'S':
        break
print('==' * 20)
print(f'Foi digitado um total de {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Em ordem decrescente fica {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na Lista.')
else:
    print('O valor Nao foi encontrado na Lista.')
