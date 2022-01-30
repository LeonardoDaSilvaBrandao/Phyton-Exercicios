#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


produto1 = str(input('Digite o nome do Primeiro produto R$'))
produto2 = str(input('Digite o nome do Segundo produto R$'))
produto3 = str(input('Digite o nome do Tercerio produto R$'))

p1 = float(input('Digite o preço do primeiro produto R$'))
p2 = float(input('Digite o preço do segundo produto R$'))
p3 = float(input('Digite o preço do terceiro produto R$'))

if p1 < p2 and p3:
    print(f'O produto mais barato é o {produto1}')
    input('Pressione ENTER para encerrar o programa.')
    exit()

if p2 < p3 and p1:
    print(f'O produto mais barato é o {produto2}')
    input('Pressione ENTER para encerrar o programa.')
    exit()

if p3 < p2 and p1:
    print(f'O produto mais barato é o {produto3}')
    input('Pressione ENTER para encerrar o programa.')
    exit()

elif p1 == p2 and p3:
    print('Todos os produtos tem preços iguais.')
    input('Pressione ENTER para encerrar o programa.')
    exit()

else:
    print('Algo deu errado, tente novamente.')
    input('Pressione ENTER para encerrar o programa.')
    exit()
