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
        for LINHA in a:
            dado = LINHA.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'NOME : {dado[0]:<30}{dado[1]:>3} ANOS')
        linha()
    finally:
        a.close()


def cadastrarNovo(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever os dados')
        else:
            print('Novo Cadastro com Sucesso!')
    linha()