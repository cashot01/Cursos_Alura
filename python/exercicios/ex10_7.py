import os
os.system("cls")
"""
7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""
valores = [10, 25, 77, 12, 100]
try:
    soma = sum(valores)
    quantidade = len(valores)
    media = soma / quantidade
    print(media)
except:
    print("Lista vazia ou numero 0")

