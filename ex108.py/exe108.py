#copia do exercicio 107 mas usando agora modulo dentro de uma pasta
import utilitario 

preco = int(input('Digite um preço R$ :'))
print(f'A metade do preço é R$ {utilitario.metade(preco):.2f}')
print(f'O dobro do preço é R$ {utilitario.dobro(preco):.2f}')
print(f'Com 10% a mais fica R$ {utilitario.aumento10(preco):.2f} (teve um aumento de R${utilitario.aumento10(preco) - preco:.2f})')
