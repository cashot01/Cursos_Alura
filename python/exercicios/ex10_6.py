import os
os.system("cls")
"""
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
"""
soma = 0
numeros = [10, 23, 55, 73, 10, 20]
for numero in numeros:
    
    try:
        soma += numero
        
    except:
        print("não é um numero")
    
print(soma)
