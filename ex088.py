from random import randint
jogos = []
print('--' * 20)
print(f'{"MEGA-SENA":^40}')
print('--' * 20)
jogo = int(input('Quantos jogos deseja : '))
print('=-' * 5,'SORTEANDO JOGOS','=-' * 5)
for c in range(jogo):
    cartela = []
    for j in range(6):
        valor = randint(1,10)
        cartela.append(valor)
    jogos.append(cartela[:])
for cartelas in enumerate(jogos):
    print(f'JOGO {cartelas[0] + 1} : {cartelas[1]}')
print('=-' * 20)
