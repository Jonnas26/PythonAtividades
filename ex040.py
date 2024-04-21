nota1 = int(input('Qual suas 1º nota:'))
nota2 = int(input('Qual suas 2º nota:'))
#Calculando média e sabendo o resultado#
media = (nota1 + nota2)/2
if media < 5:
    print('Reprovado!')
elif 5 < media < 7:
    print('Recuperação!')
else:
    print('Aprovado!')
