import math

#4 Crie um programa que recebe três valores inteiros pelo teclado e imprime qual dos três é menor

x = int(input("digite o primeiro número \n"))
y = int(input("digite o segundo número \n"))
z = int(input("digite o terceiro número \n"))

if x < y and x < z:
    print(f"o número {x} é menor que o {y} e {z}")
elif y < x and y < z:
    print(f"o número {y} é menor que o {x} e {z}")
elif z < x and z < y:
    print(f"o número {z} é menor que o {x} e {y}")
elif x == y and x < z:
    print(f"os números {x} são menores que {z}")
elif y == z and y < x:
    print(f"os números {y} são menores que {x}")
elif z == x and z < y:
    print(f"os números {z} são menores que {y}")
else:
    print(f"os números são iguais")