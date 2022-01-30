n1 = int(input('Digite o primeiro número inteiro: '))

n2 = int(input('Digite o segundo número inteiro: '))

n3 = int(input('Digite o terceiro número inteiro: '))

if n1 > n2 and n3:
    print(f'O maior número é {n1}')
    input('Pressione ENTER para encerrar programa')

if n2 > n1 and n3:
    print(f'O maior número é {n2}')
    input('Pressione ENTER para encerrar programa')
    exit()

if n3 > n1 and n2:
    print(f'O maior número é {n3}')
    input('Pressione ENTER para encerrar programa')
    exit()