tamanho = float(input('tamanho do arquivo (MB) a ser baixado: '))

Velocidade = float(input('Velocidade da internet (MBPS): '))

tempo = tamanho / Velocidade

Minuto = tempo / 60

print(f'O download ira durar {Minuto:.2f} Minutos ou {tempo:.2f} Segundos')

input('Pressione enter para encerrar o programa...')