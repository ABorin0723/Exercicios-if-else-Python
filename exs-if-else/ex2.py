import math

#2 Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.

x = int(input("digite o primeiro número "))
y = int(input("digite o segundo número "))

if x > y:
    print(f"o número {x} é maior que o {y}")
elif x < y:
    print(f"o número {y} é maior que o {x}")
else:
    print(f"o número {x} é igual ao número {y}")