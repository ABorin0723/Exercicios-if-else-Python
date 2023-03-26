import math

#8  Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:
# • Digite 1 para somar dois valores
# • Digite 2 para subtrair dois valores
# • Digite 3 para multiplicar dois valores
# • Digite 4 para dividir dois valores
# • Digite 5 para realizar uma potência entre dois valores
# • Digite 6 para realizar uma radiciação entre dois valores
# • Digite qualquer outro número para sair
# De acordo com a opção informada pelo usuário, solicite os valores necessários para o
# usuário e imprima na tela o resultado da operação realizada.

print("operações básicas com 2 valores. Digite: \n")
num = int(input(" 1 para somar \n 2 para subtrair \n 3 para multiplicar \n 4 para dividir \n 5 para potencia \n 6 para raiz \n outro para sair \n "))

if num >= 1 and num <= 6:
    a = float(input("digite o primeiro valor"))
    b = float(input("digite o segundo valor"))

    def conta(a,b):

        if num == 1:
            print(a+b)
        elif num == 2:
            print(a-b)
        elif num == 3:
            print(a*b)
        elif num == 4:
            print(a/b)
        elif num == 5:
            print(a**b)
        else:
            print(a%b)

    conta(a,b)
else:
    print("voce saiu")
