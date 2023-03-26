import math

#10 Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.

vogais = ["a","e","i","o","u"]

letra = input("digite uma letra \n")

if letra in vogais:
    print("é vogal")
else:
    print("é consoante")