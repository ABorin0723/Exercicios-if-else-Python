import math

#3 Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B. Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.

A = int(input("digite o primeiro número "))
B = int(input("digite o segundo número "))

if B != 0:
    print(f"{A/B:.0f}")
else:
    print("erro, o valor B não pode ser igual a zero")