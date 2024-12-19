alunos = []
aluno = []
while True:
    nome = str(input('Digite o nome de aluno: '))
    nota1 = float(input('Digite a nota dele : '))
    nota2 = float(input('Digite a segunda nota: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    alunos.append(aluno[:])
    aluno.clear()
    continuar = str(input('Tem mais algum aluno para cadastra? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print(alunos)
print('=-' * 30)
print(f'{'CODIGO'}  {'ALUNOS'}{'MÉDIA':>25}')
print('=-=' * 20)
for i,v in enumerate(alunos):
    print(f'{i:>3}{v[0]:>11}{v[1]+v[2]/2:>25}')
while True:
    visualizar = int(input('Qual aluno deseja ver separadamente [999 INTERROMPE]:'))
    if visualizar == 999:
        break   
    print(f'ALUNO {alunos[visualizar][0]}        1° NOTA {alunos[visualizar][1]:.2f} / 2° NOTA {alunos[visualizar][2]:.2f} / MÉDIA = {alunos[visualizar][1] + alunos[visualizar][2]/2:.2f}')


