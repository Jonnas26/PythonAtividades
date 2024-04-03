from random import randint
pc = randint(0,5)
escolha = int(input('Escolha um numero de 0 a 5 :'))
print('!Se você acertar o que eu pensei você ganha!')
if escolha == pc:
    print('Você acertou o numero que pensei parabens!')
else:
    print('Você errou, não foi o numero que pensei. ')
    