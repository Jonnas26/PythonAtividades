time = []
jogador = {}
gols = []
while True:
    tot = 0
    jogador.clear()
    jogador['Nome'] = str(input('Qual o nome do jogador :'))
    jogos = int(input('Quantas partidas ele jogou :'))
    for j in range(0,jogos):
        gol = int(input('Gols :'))
        tot += gol
        gols.append(gol)
    jogador['Gols'] = gols[:]
    jogador['Total'] = tot
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    time.append(jogador.copy())
    gols.clear()
    tot -= tot
    if cont in 'N':
        break
print('cod  ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('=-' * 20)
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15} ',end='')
    print()
while True:
    busca = int(input('Qual jogador deseja ver separado pelo codigo [999 para parar]:'))
    print('--' * 20)
    if busca == 999:
        break
    if busca >= len(time):
        print('Não tem nenhum jogador com esse codigo!')
    print(f'Aqui esta o dados do jogador {time[busca]["Nome"]}')
    for j, g in enumerate(time[busca]["Gols"]):
        print(f'   No jogo {j + 1} fez {g} gols.')
