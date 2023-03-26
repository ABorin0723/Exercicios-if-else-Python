import math

# 6 Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado. A taxa aplicada deve ser:
# • Aumento de 10% caso o valor seja menor do que 100
# • Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
# • Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
# • Imprima uma mensagem de erro se o valor for negativo
# • Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

preço = float(input("preço: "))

def juros(preço):

    while preço <= 0:
        print("valor não pode ser negativo nem 0")
        preço = float(input("preço: "))
    if preço > 0 and preço < 100:
        print(f"o preço {preço}, com juros de 10% é {preço * 1.1:.2f}")
    elif preço >= 100 and preço < 300:
        print(f"o preço {preço}, com juros de 20% é {preço * 1.2:.2f}")
    elif preço >= 300 and preço < 1000:
        print(f"o preço {preço}, com juros de 50% é {preço * 1.5:.2f}")
    else:
        print(f"o preço é {preço:.2f}")

juros(preço)