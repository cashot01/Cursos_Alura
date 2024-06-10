import os
os.system("cls")
"""
3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""
soma_impar = 0
for numero in range(1, 11):

    if numero % 2 == 1:
        soma_impar += numero
print(soma_impar)       
    