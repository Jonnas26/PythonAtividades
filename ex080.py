#Ordenando um Lista sem usar o Sort
lista = []
for c in range(0,4):
    n = int(input('Digite um numero:'))
    if c == 0 or n > lista[-1]:
        lista.append(n) 
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1
print(lista)
