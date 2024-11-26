from random import randint
vitoria = 0
print('--' * 20)
print('JOGO DO IMPAR OU PAR')
print('--' * 20)
while True:
    pc = randint(1,10)
    jogada = int(input('Escolha um numero:'))
    escolha = ' '
    while escolha not in 'IP':
        escolha = str(input('IMPAR ou PAR [I/P]:')).strip().upper()[0]
    soma = pc + jogada
    print(f'Você escolheu {jogada} e o Computador {pc} ')
    print(f'E o total é de {soma}.')
    if soma % 2 == 0:
        if escolha == 'I':
            print('Assim deu PAR e você perdeu.')
            break
        else:
            print('Você ganhou,vamos novamente!')
            vitoria += 1
    elif soma % 2 == 1:
        if escolha == 'P':
            print('Assim deu IMPAR e você perdeu.')
            break
        else:
            print('Você ganhou, vamos novamente!')
            vitoria += 1
print(f'Você teve a sequencia de {vitoria} vitorias seguidas.')
