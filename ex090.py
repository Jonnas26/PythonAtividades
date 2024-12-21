#Primeira atividade usando Dicionario
pessoa = {}
pessoa['Nome'] = str(input('Qual o seu nome :'))
pessoa['Média'] = float(input('Qual a sua média :'))
if pessoa['Média'] >= 7 :
    pessoa['Situação'] = 'Aprovado'
elif 5 <= pessoa['Média'] < 7:
    pessoa['Situação'] = 'Recuperação' 
else:
    pessoa['Situação'] = 'Reprovado'
print('=-' * 20)
for k,v in pessoa.items():
    print(f'    - {k} é igual {v} .')
