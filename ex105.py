def notas(* núm, sit=False):
    aluno = {}
    aluno['Total'] = len(núm) 
    maior = menor = 0
    for n in range(0, len(núm)):
        if n == 0:
            maior = núm[n]
            menor = núm[n]
        elif núm[n] > maior:
            maior = núm[n]
        elif núm[n] < menor:
            menor = núm[n]
    aluno['Maior'] = []
    aluno['Menor'] = []
    aluno['Maior'].append(maior)
    aluno['Menor'].append(menor)
    aluno['Média'] = sum(núm)/ len(núm)
    if sit == True:
        aluno['Situação'] = []
        if aluno['Média'] > 8 :
            aluno['Situação'] = 'Situação Boa'
        if 6 < aluno['Média'] < 8:
            aluno['Situação'] = 'Situação Razoavel'
        else:
            aluno['Situação'] = 'Situação RUIM'    
        return aluno


resp = notas(3, 6, 12 , sit= True)
print(resp)
