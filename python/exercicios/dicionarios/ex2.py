import os
os.system("cls")
"""
Utilizando o dicionário criado no item 1 (Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.):

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
"""
pessoa = {"nome": "Cauan",
        "idade": 18, 
        "cidade": "São Paulo"}
print(pessoa)
print()

pessoa["idade"] = 25

pessoa["profissão"] = "Pedreiro"

del pessoa["cidade"]

print(pessoa)