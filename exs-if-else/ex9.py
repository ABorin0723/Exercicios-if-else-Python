import math

#9 (adaptado) Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C. Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o cálculo.

gA = float(input("Digite a nota do grau A: "))

while gA < 0 or gA > 3:
    print("Nota inválida.")
    gA = float(input("Digite a nota do grau A: "))

gB = float(input("Digite a nota do grau B: "))

while gB < 0 or gB > 10:
    print("Nota inválida.")
    gB = float(input("Digite a nota do grau B: "))

soma = gA + gB

if soma < 7:
    gC = float(input("É necessário fazer o grau C. Digite a nota do grau C: "))
    
    while gC < 0 or gC > 10:
        print("Nota inválida.")
        gC = float(input("Digite a nota do grau C: "))
    
    media = (soma + gC) / 2

    if media < 7:
        print("Você não passou.")
    else:
        print("Você passou.")
else:
    print("Você passou.")