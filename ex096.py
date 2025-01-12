def area(larg, comp):
    a = larg * comp
    print(f'A area total de {larg:.2f} x {comp:.2f} é de {a:.2f}.')


print('Medindo terreno')
l = float(input('Largura (m) :'))
c = float(input('Comprimento (m) :'))
area(l,c)