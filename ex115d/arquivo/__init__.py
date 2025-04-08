from funções import cabeçalho


def abrirArquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Não foi possivel criar arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao abrir tabela de usuarios cadastrados.')
    else:
        cabeçalho('LISTA DE USUARIOS CADASTRADOS')
        for LINHA in a:
            dado = LINHA.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].upper():<30} {dado[1]:>3} ANOS')
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