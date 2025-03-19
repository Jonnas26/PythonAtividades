#Usando agora o novo pacote DADO para validar a entrada
from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro('Digite um valor:')
moeda.resumo(p, 70,25)
