print('-' * 20)
print('TABUADA')
print('-' * 20)
while True:
    num = int(input('Digite um numero[Digite algum numero negativo para parar]:'))
    if num < 0:
        break
    for n in range(1,11):
        print(f'{n:<2} x {num:<2} = {n * num}')
    print('-' * 20)
print('FIM')
