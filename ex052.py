#SABENDO SE UM NUMERO É PRIMO#
tot = 0
num = int(input("Digite um numero:"))
for c in range(1,num+1):
    #MOSTRA AS VEZES QUE ELE FOI DIVISIVEL E FICA VERMELHO#
    if num % c == 0:
        print(f'\033[91m{c}\033[0m',end=' ')
        tot += 1
    #SE NÃO FOI DIVISIVEL FICA EM AZUL#
    else:
        print(f'\033[94m{c}\033[0m',end=' ')
if tot > 2:
    print(f'\nO numero {num} não é primo\nPois se dividiu {tot} vezes.')
else:
    print(f'\nO numero {num} é primo\nPois ele se dividiu apenas 2 vezes.')

