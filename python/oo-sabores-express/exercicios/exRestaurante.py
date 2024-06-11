import os
os.system("cls")
# class = classe 
class Restaurante:
    # atributos da classe
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"




restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))