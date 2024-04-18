from datetime import datetime
anonasc = int(input('Em que ano você nasceu :'))
#Sabendo a idade e se ja passou,não chegou ou esta na hora de se alistar#
anoatual = datetime.today().year
idade = anoatual - anonasc
if idade == 18:
    print('Esta na hora de ser Alistar garoto .')
elif idade < 18:
    print('Você ainda não precisa se alistar .')
elif idade > 18 :
    print(f'Você esta atraso a {idade - 18} anos de se Alistar garoto.')
