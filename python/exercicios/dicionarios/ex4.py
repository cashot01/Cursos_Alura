import os
os.system("cls")
"""
4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
"""

pessoa = {"nome": "Andrea", 
          "idade": 20, 
          "cidade": "Osasco"}
print(pessoa)

if "estado" in pessoa:
    print("Chave (estado) existe ")
else:
    print("Chave (estado) não existe")