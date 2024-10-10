sexo = str(input('Qual seu sexo: [F/M]')).upper()
#looping ate que o valor digitado acima seja feito
while sexo not in 'FM':
    if sexo not in 'FM':
        print('Digite novamente usando F ou M para seu sexo.')
        sexo = str(input('Qual seu sexo: [F/M]')).upper()
print('fim')