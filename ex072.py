numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    escolha = int(input('Digite um numero de 0 a 20 :'))
    if 0 >= escolha <= 20:
        break
    print('Faça a escolha que se pede a cima!')
print(f'Você digitou o numero {numeros[escolha]}.')
