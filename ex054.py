maioridade = menoridade = 0
#importando o ano atual e definindo um objeto para ele
from datetime import date
hoje = date.today().year
#criando o laço para saber o ano de nascimento de cada pessoa
for c in range(0,7):
    ano = int(input('Em que ano nasceu?'))
#sabendo a idade ao subtrair o ano atual com o nascimento
    if hoje - ano >= 18:
        maioridade += 1
    elif hoje - ano < 18:
        menoridade += 1
print(f'Tem {maioridade} pessoas acima ou igual a 18 anos.'
      f'E tem {menoridade} pessoa menores de 18 anos.')
