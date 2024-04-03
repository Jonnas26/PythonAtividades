frase = str(input('Digite uma frase qualquer:')).strip().upper()
print(f'A letra (a) aparece {frase.count("A")} vezes.')
print(f'A letra (a) aparece pela primeira vez na posição {frase.find("A") + 1}.')
print(f'A letra (a) aparece pela ultima vez na posição {frase.rfind("A") }')
