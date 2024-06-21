from veiculo import Veiculo

"""
3) No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
"""

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
        self._status = "Desligado"
    
    def __str__(self):
        return f" Marca: {self._marca} | Modelo: {self._modelo} | Cor: {self.cor} | Status: {self._status}"
    
    def ligar(self):
        self._status = "Ligado"