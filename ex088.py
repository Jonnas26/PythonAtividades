from random import randint
from time import sleep
jogos = []
cartela = []
print('--' * 20)
print(f'{"MEGA-SENA":^40}')
print('--' * 20)
quant = int(input('Quantos jogos deseja : '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0,60)
        if num not in cartela:
            cartela.append(num)
            cont += 1
        if cont == 6:
            break
    cartela.sort()
    jogos.append(cartela[:])
    cartela.clear()
    tot += 1
print('SORTEANDO JOGOS')
for i,v in enumerate(jogos):
    print(f'{i + 1}° jogo : {v}')
    sleep(1)
print('BOA SORTE!')
