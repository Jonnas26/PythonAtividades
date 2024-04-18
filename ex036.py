casa = int(input('Digite o valor da casa que deseja comprar: R$'))
anos = int(input('Em quanto anos vai pagar esse imovel? :'))
salario = float(input('Qual o valor do seu salario R$: '))
parcela =  casa / (anos*12)
#Calculo para verificar se o valor da porcentagem do salario(30%) consegue pagar as parcelas da casa durante o periodo#
salarioparcela = (salario * 30) / 100
if salarioparcela >= parcela:
    print('É possivel fazer o emprestimo !')
else:
    print('Não é possivel fazer o emprestimo. ')
