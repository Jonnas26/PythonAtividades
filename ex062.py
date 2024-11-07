#PROGRESSÂO ARITMÉTICA COM WHILE E BOTAO DE PARE DO USUARIO#
primt = int(input('Qual o primeiro termo:'))
razao = int(input('Qual a razão:'))
termo = primt
cont = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont < total:
        print(f'{termo} > ' ,end='')
        termo += razao
        cont += 1
    print('Pausa')
#    BOTAO DE PARE DO USUARIO#
    mais = int(input('Quantos termos a mais deseja ver : [0 para parar]'))
    print(f'{termo} > ' ,end='')
    termo += razao
    cont += 1
print('FIM')
