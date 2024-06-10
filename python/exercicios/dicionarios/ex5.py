import os
os.system("cls")
"""
5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
"""
frase = "Cauan Cauan Caique Andrea."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
