from random import choice
nome1 = str(input('Nome do 1º aluno:'))
nome2 = str(input('Nome do 2º aluno:'))
nome3 = str(input('Nome do 3º aluno:'))
lista = [nome1,nome2,nome3]
print(f'O aluno escolhido foi {choice(lista)}')
