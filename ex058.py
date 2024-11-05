from random import randint
computador = randint(1,10)
tentativas = 0
print(computador)
print('Tente adivinhar o numero que pensei!')
print('Pensei em um numero entre 1 e 10.')
while True:
    escolha = int(input('Digite um numero:'))
    if escolha < 11:
        tentativas += 1
    elif escolha > 10:
        print('Digite um numero entre 1 e 10!')
    if escolha == computador:
        break
print(tentativas)
