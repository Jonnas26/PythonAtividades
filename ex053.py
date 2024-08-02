frase = str(input("Digite uma frase :")).strip().upper()
#primeiro separamos cada palavra da frase
palavra = frase.split()
#depois juntamos todas sem espaço
junto = ''.join(palavra)
#comparamos se ela normal é a mesma ao contrario
if junto == junto[::-1]:
    print('è um palindromo.')
else:
    print('nâo é um palindromo,')
