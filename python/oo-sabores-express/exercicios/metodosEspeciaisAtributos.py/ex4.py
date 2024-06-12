import os
os.system("cls")
"""
Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
"""
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

restaurante1 = Restaurante("MC Donalds", "Humburgueria",)
restaurante2 = Restaurante("Emporio", "Prato feito")

Restaurante.listar_restaurantes()