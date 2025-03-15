#primeira atividade usando um modulos *util.py*
import util

preco = int(input('Digite um preço R$ :'))
print(f'A metade do preço é {util.metade(preco):.2f}')
print(f'O dobro do preço é {util.dobro(preco):.2f}')
print(f'Com 10% a mais fica {util.aumento10(preco):.2f} (teve um aumento de R${util.aumento10(preco) - preco:.2f})')
