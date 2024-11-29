##Fazendo buscas dentro de um Tupla
times = ('Botafogo','Palmeiras','Internacional','Fortaleza','Flamengo',
         'São Paulo','Cruzeiro','Bahia','Corinthians','Atlético-MG',
         'Vasco','EC Vitoria','Juventude','Grêmio','Athletico-PR',
         'Fluminense','Criciúma','Bragantino','Cuiabá','Atlético-GO')
print('==' * 20)
print('Aqui a lista do TOP 5 do Brasileirão:')
for top5 in range(0,5):
    print(f'{top5 + 1}° Lugar : {times[top5]}')
print('==' * 20)
print('Aqui a lista do ultimos 4 da tabela:')
for ult4 in range(-4,0):
    print(f'Em {21 + ult4}° Lugar : {times[ult4]}')
print('==' * 20)
print('Em ordem Alfabética a tabela fica:')
print(sorted(times))
print('==' * 20)
print(f'E a posição que o Atlético mineiro esta na tabela é a {times.index('Atlético-MG') + 1}° posição')
