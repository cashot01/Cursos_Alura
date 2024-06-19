from veiculo import Veiculo
from carro import Carro
from moto import Moto

"""
7. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

9. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método **str**.
"""

carro1 = Carro("BMW", "X6", 4)
carro2 = Carro("Fiat", "Uno", 2)
carro3 = Carro("Nissan", "Skyline", 4)

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "MT-09", "Esportiva")



print(carro1)
print(carro2)
print(carro3)
print()
print(moto1)
print(moto2)
print(moto3)