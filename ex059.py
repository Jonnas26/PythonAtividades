from time import sleep
maior = menor = 0
escolha = 0
n1 = int(input('Digite um numero   :'))
n2 = int(input('Digite outro numero:'))
while escolha != 5:
    print('''[1] SOMAR
[2] MULTPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR ''')
    escolha = int(input('O que deseja fazer :'))
    print('==='*10)
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma de {n1}+{n2} é {soma}.')
    elif escolha == 2:
        mult = n1 * n2
        print(f'A multiplicação de {n1}x{n2}= {mult}')
    elif escolha == 3:
        if n1 > n2:
            n1 = maior
        else:
            n2 = maior
    elif escolha == 4:
        n1 = int(input('Escolha um novo numero:'))
        n2 = int(input('Escolha outro novo numero:'))
    sleep(1)
print('Ate a proxima.')
