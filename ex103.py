def jogador(a='<desconhecido>', b=0):
    if not a:
        a = '<desconhecido>'
    if not b:
        b = 0
    return f'O jogador {a} fez {b} gols no campeonato.'


nome = input('Qual o nome do jogador:').strip()
gols = input('Quantos gols ele fez  :')
print(jogador(a=nome, b=gols))
