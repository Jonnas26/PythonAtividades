from datetime import datetime
ano = datetime.today().year
nasc = int(input('Em que ano nasceu? :'))
#SABENDO A CATEGORIA BASEADO NA IDADE#
idade = ano - nasc
if idade <= 9:
    print('CATEGORIA : MIRIM')
elif 9 <= idade <= 14:
    print('CATEGORIA : INFANTIL')
elif 14 <= idade <= 19:
    print('CATEGORA : JUNIOR')
elif 19 <= idade <= 25:
    print('CATEGORIA : SÊNIOR')
else:
    print('CATEGORIA : MASTER')
