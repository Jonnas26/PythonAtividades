from random import randint
from operator import itemgetter
from time import sleep
rank = []
jogadores = {'jogador1' : randint(1,6),
             'jogador2' : randint(1,6),
             'jogador3' : randint(1,6),
             'Jogador4' : randint(1,6)}
print('==' * 20)
print('RANKING DOS JOGADORES')
print('==' * 20)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse= True)
for i,v in enumerate(rank):
    print(f'{i + 1}° Lugar : {v[0]} tirou {v[1]} nos dados.')
    sleep(1)
print('==' * 20)
