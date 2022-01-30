nome = str(input('Digite o nome do aluno: ')) 

nota1 = float(input('Digite a primeira nota do aluno: '))

nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) /2 

if media==7:
    print(f'{nome} foi Aprovado(a)')
    input('Pressione enter para encerrar o programa.')
    exit()

if media==8:
    print(f'{nome} foi Aprovado(a)')
    input('Pressione enter para encerrar o programa.')
    exit()

if media==9:
    print(f'{nome} foi Aprovado(a)')
    input('Pressione enter para encerrar o programa.')
    exit()

elif media==10:
    print(f'{nome} foi Aprovado(a) com distinção.')
    input('Pressione enter para encerrar o programa.')
    exit()

else:
    print(f'{nome} foi Reprovado(a)')
    input('Pressione enter para encerrar o programa...')
    exit()