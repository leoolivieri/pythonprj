#!/usr/bin/env python3

autor = "Leonardo Olivieri"

#Lista: é uma sequência ordenada de valores

portas_alvo = [22, 80, 443, 3306, 8080, 3000, 5000, 137, 138, 139, 445]
portas_alvo.append(21) #Adiciona a porta 21 na variável portas_alvo
servicos = ["ssh", "https", "dns"]

print("A lista de portas é: ", portas_alvo)
print( f'A lista de portas é: {portas_alvo}')


print( " O índice 2, tem valor: ", portas_alvo[2])
print( " O índice -1, tem valor: ", portas_alvo[-1])


for NUM in range(1,11):
	print(NUM)

# Dicionários

status_servico = {
	'host': '8.8.8.8',
	'porta': '443',
	'estado': 'aberta',
	'servico': 'https'
}

print(status_servico['host'])
print(status_servico['servico'])

servicos = {22:'SSH', 80: 'HTTP', 443: 'HTTPS', 3306: 'MYSQL', 'DNS': 53}

for PORTA in portas_alvo:
	nome = servicos.get(PORTA, 'desconhecido')
	print(f'Porta {PORTA}: Servico {nome}')
