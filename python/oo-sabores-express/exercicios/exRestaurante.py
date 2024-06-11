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
restaurante_praca.categoria = "Italiana"

if restaurante_praca.ativo:
    print(f"Restaurante está ativo")
else:
    print(f"Restaurante está desativado")

categoria = restaurante_praca.categoria
restaurante_praca.nome = "Bistrô"




restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print()
print(vars(restaurante_pizza))