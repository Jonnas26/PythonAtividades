from random import randint
num = randint(1,3)
print('ESCOLHA\n[1]PEDRA\n[2]PAPEL\n[3]TESOURA')
escolha = int(input('O QUE VAI ESCOLHER :'))
print(num)
if escolha == 1 and num == 1:
    print('DEU EMPATE AMBOS ESCOLHERAM PEDRA!')
elif escolha == 1 and num ==2:
    print('O COMPUTADOR VENCE ELE ESCOLHEU PAPEL!')
elif escolha == 1 and num == 3:
    print('VOCÊ VENCEU ! O COMPUTADOR ESCOLHEU TESOURA.')
if escolha == 2 and num == 1:
    print('VOCÊ VENCEU ! O COMPUTADOR ESCOLHEU PEDRA.')
elif escolha == 2 and num ==2:
    print('DEU EMPATE AMBOS ESCOLHERAM PAPEL!')
elif escolha == 2 and num == 3:
    print('O COMPUTADOR VENCE ELE ESCOLHEU TESOURA!')

