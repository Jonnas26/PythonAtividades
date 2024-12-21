from datetime import datetime
ano = datetime.now().year
dados = {}
while True:
    dados['Nome'] = str(input('Qual o nome :'))
    nascimento= int(input('Ano de nascimento :'))
    dados['Idade'] = ano - nascimento
    dados['CTOS'] = int(input('Carteira de Trabalho (0 se não tiver) :'))
    if dados['CTOS'] == 0:
        print('==' * 20)
        for k,v in dados.items():
            print(f'{k} tem o valor {v}.')
        break
    dados['Contratação'] = int(input('Qual o ano de contratação :'))
    dados['Salario'] = float(input('Qual o seu salario :'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - ano)
    print('=-=' * 15)
    for k,v in dados.items():
        print(f'{k} tem o valor {v}.')
    break
print('==' * 20)