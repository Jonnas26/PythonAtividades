pessoa = {}
pessoa['Nome'] = str(input('Qual o seu nome :'))
pessoa['Média'] = float(input('Qual a sua média :'))
if pessoa['Média'] >= 7 :
    pessoa['Situação'] = 'Aprovado'
else:
    pessoa['Situação'] = 'Reprovado'
print('=-' * 20)
print(pessoa)
for k,v in pessoa.items():
    print(f'    -{k} é igual {v} .')
