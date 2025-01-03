pessoa = {}
galera = []
soma = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Qual seu nome : '))
    pessoa['Idade'] = int(input('Qual sua idade :'))
    soma += pessoa['Idade']
    while True:
        pessoa['Sexo'] = str(input('Qual seu sexo [F/M]')).strip().upper()[0]
        if pessoa['Sexo'] in 'FM':
            break
        print('ERRO! Digite F ou M.')
    galera.append(pessoa.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if cont == 'N':
        break
print('=-' * 20)
print(f'A) No total foram cadastradas {len(galera)}')
print(F'B) A média de todas as idades  é de {soma/len(galera)}')
print('C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']}',end=' ')
    print()
print('Essas pessoas possuem uma idade acima da media ',end='')
for p in galera:
    if p['Idade'] >= soma/len(galera) :
        print(f'{p['Nome']}',end=' ')
