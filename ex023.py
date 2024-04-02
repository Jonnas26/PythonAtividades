num = int(input('Digite um numero com 4 casas:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade de {num} é {u}.')
print(f'A dezena de {num} é {d}.')
print(f'A centena de {num} é {c}.')
print(f'A milhar de {num} é {m}.')
