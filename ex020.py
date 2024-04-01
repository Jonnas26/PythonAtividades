from random import shuffle
nome1 = str(input('Nome do 1º aluno:'))
nome2 = str(input('Nome do 2º aluno:'))
nome3 = str(input('Nome do 3º aluno:'))
lista = [nome1, nome2, nome3]
shuffle(lista)
print(f'Nova ordem é de {lista}')
