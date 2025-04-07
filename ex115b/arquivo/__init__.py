from funçoes import linha


def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criaArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criaçao do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso')

        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        linha()
        print(f"{'[1] VER PESSOAS CADASTRADAS':^30}")
        print(a.read())
        a.close()
        linha()

