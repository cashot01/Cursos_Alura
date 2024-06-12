import os
os.system("cls")
"""
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
"""
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo, telefone, cidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.telefone = telefone
        self.cidade = cidade
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo} | {self.telefone} | {self.cidade}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.telefone} | {restaurante.cidade}")

restaurante1 = Restaurante("MC Donalds", "Humburgueria", "ativo", 987654321, "Osasco")
restaurante2 = Restaurante("Emporio", "Prato feito", "desativado", 123456789, "Embu das Artes")

Restaurante.listar_restaurantes()