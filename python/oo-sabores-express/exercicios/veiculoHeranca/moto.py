from veiculo import Veiculo
"""
5. Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

6. Implemente o Método Especial **str** na Classe Filha (Moto): Adicione um método especial **str** à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
"""

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
        # tipo = esportiva ou casual

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self.marca} {self.modelo} - Tipo: {self.tipo} - Status: {status}"
    
