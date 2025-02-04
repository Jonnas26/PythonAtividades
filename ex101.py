def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - nasc
    if idade >= 18:
        return f'Com {idade} anos : VOTO OBRIGATORIO!'
    elif idade < 16:
        return f'Ainda não é possivel votar com {idade} anos.'
    else:
        return f'Voto Opcional com {idade} anos.'


nasc = int(input('Que ano nasceu? '))
print(voto(nasc))
