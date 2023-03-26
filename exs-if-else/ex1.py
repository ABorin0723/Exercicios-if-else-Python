import math

#1  Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

x = int(input("digite um numero inteiro "))

if x % 2 == 0:
    print("o número é par")
else:
    print("o número é ímpar")