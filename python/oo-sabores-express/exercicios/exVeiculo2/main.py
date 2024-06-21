# from veiculo import Veiculo
from carro import Carro

"""
4) Em um arquivo chamado main.py, importe a classe Carro.

5) No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
"""

carro1 = Carro("BMW", "X6", "Preta")
carro2 = Carro("Ferrari", "LaFerrari", "Veermelha")
carro3 = Carro("Toyota", "Supra MK4", "Laranja")
print(carro1)
print(carro2)
print(carro3)

carro1.ligar()
carro2.ligar()
carro3.ligar()

print()
print(carro1)
print(carro2)
print(carro3)