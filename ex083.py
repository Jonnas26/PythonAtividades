expressao = str(input('Digite uma expressão :'))
pilha = []
for simb in expressao:
    if simb in '(':
        pilha.append(simb)
    elif simb in ')':
        pilha.append(simb)
if len(pilha) % 2 == 0:
    print('Expressão valida.')
else:
    print('Expressão invalida.')
