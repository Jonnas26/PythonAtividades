casa = int(input('Digite o valor da casa que deseja comprar: R$'))
anos = int(input('Em quanto anos vai pagar esse imovel? :'))
salario = float(input('Qual o valor do seu salario R$: '))
parcela =  casa / (anos*12)
salarioparcela = (salario * 30) / 100
if salarioparcela >= parcela:
    print('É possivel fazer o emprestimo !')
else:
    print('Não é possivel fazer o emprestimo. ')
