import math

#7 Crie um programa que recebe um valor inteiro referente a um determinado dano. Impmrima na tela se o ano informado é bissexto ou não

ano = int(input("digite um ano "))

if ano % 4 == 0:
    print("o ano é bissexto")
else:
    print("o ano não é bissexto")