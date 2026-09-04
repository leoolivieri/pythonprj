#!/usr/bin/env python3

notas = []
soma = 0

for nota in range(1, 6):
    while True:
        try:
            nota2 = float(input(f"Digite a nota {nota} de 5: "))
            notas.append(nota2)
            soma += nota2
            break
        except ValueError:
            print("Digite apenas números!")

for nota in range(5):
    print("Nota %d: %.2f" % (nota + 1, notas[nota]))

print("A Média é %.2f" % (soma / 5))
