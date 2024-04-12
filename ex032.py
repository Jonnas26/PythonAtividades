from datetime import datetime
atual = datetime.today().year
ano = int(input('Digite um ano:'))
# Como calcular um ano bissexto #
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('Não é um ano bissexto.')
# Caso queira saber do ano atula #
escolha = int(input('Digite 1 se quiser saber se o ano atual é bissexto.'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('Não é um ano bissexto.')
