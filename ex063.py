print('--' * 20)
print('SEQUENCIA DE FIBONACCI')
print('--' * 20)
num = int(input('Digite um numero :'))
print('~~' * 20)
t1 = 0
t2 = 1
print(f'{t1} > {t2} > ',end='')
cont = 3
while cont < num:
    t3 = t1 + t2
    print(f'{t3} > ',end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
