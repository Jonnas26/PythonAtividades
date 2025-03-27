import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br')
except urllib.erro.URLError:
    print('O site não esta disponivel.')
else:
    print('O site esta disponivel para consulta')
