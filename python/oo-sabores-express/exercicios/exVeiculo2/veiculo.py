import os
os.system("cls")
from abc import ABC, abstractmethod

"""
1) Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

2) No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
Crie uma nova classe chamada Carro que herda da classe Veiculo.

3) No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

4) Em um arquivo chamado main.py, importe a classe Carro.

 5) No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
"""

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._status = "Desligado"

    def __str__(self):
        return f" Marca: {self._marca} | Modelo: {self._modelo}"
    
    @abstractmethod
    def ligar(self):
        pass