expressao = str(input('Digite uma expressão :'))
pilha = []
for simb in expressao:
    if simb in '(':
        pilha.append(simb)
    elif simb in ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão esta correta!')
else:
    print('A sua expressão esta errada!')
    