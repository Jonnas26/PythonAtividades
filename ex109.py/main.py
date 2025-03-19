#melhorando ainda mais o exercicio 108
from funções import metade, dobro ,aumento10 , moeda

preco = int(input('Digite um preço R$ :'))
print(f'A metade do preço de {moeda(preco)} é {metade(preco , True)}')
print(f'O dobro do preço de {moeda(preco)} é {dobro(preco, True)}')
print(f'Com 10% a mais fica de {moeda(preco)} para {aumento10(preco, 10, True)}')
