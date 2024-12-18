pessoas = []
pessoa = []
tot = 0
maiorpeso = menorpeso = 0
while True:
    pessoa.append(str(input('Digite seu nome: ')))
    pessoa.append(float(input('Digite seu peso: ')))
    tot += 1
    pessoas.append(pessoa[:])
    pessoa.clear()
    stop = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if stop in 'N':
        break
maiorpeso = menorpeso = pessoas[0][1]
for peso in pessoas:
    if peso[1] > maiorpeso:
        maiorpeso = peso[1]
    elif peso[1] < menorpeso:
        menorpeso = peso[1]
print('==' * 20)
print(f'Foram cadastrados um total de {tot} pessoas .')
print(f'Maior peso foi {maiorpeso} KG, e foi de ',end=' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'{p[0]} ',end=' ')
print()
print(f'O menor peso foi de {menorpeso} KG , e foi de ', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'{p[0]}',end=' ')
