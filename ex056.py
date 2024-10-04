hvelho = ''
media = hvelhoidade = mulhermenor = 0
for L in range(0,4):
    nome = str(input('Qual seu nome:'))
    idade = int(input('Qual sua idade:'))
    sexo = str(input('Qual seu sexo: (F/M)')).strip().upper()
    media += idade
#looping que vai percorrer a cada loop e verificar se é H
    if L == 0 and sexo in 'M':
        hvelho = nome
        hvelhoidade = idade
#se tiver outro H com idade maior vai assumir a posição de mais velho
    elif sexo in 'M':
        if idade > hvelhoidade:
            hvelhoidade = idade
            hvelho = nome
#se for F e tiver menos de 20 anos sera adicionado mais 1 nessa contagem
    if sexo in 'F':
        if idade < 20:
            mulhermenor += 1
print(f'A media de todas as idades somadas é de {media/4} anos.')
print(f'O nome do homem mais velho é {hvelho}')
print(f'Tem {mulhermenor} mulheres com menos de 20 anos.')