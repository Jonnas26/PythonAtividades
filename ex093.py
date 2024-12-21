jogador = {}
gols = []
tot = 0
jogador['Nome'] = str(input('Qual o nome do jogador :'))
jogos = int(input('Quantas partidas ele jogou :'))
for j in range(0,jogos):
    gol = int(input('Gols :'))
    tot += gol
    gols.append(gol)
jogador['Gols'] = gols[:]
jogador['Total'] = tot
print('=-' * 20)
print(jogador)
print('=-' * 20)
for k,v in jogador.items():
    print(f'O Campo {k} tem o valor {v} .')
print('=-' * 20)
print(f'O jogador {jogador['Nome']} jogou {jogos} jogos .')
for i,v in enumerate(gols):
    print(f'No {i}° partida , fez {v} gols.')
print(f'E teve um total de {jogador["Total"]}gols .')
