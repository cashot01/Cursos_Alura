from modelos.cardapio.item_cardapio import ItemCardapio

"""
Crie uma classe chamada Sobremesa que herda de ItemCardapio, adicione dois atributos específicos como tipo e tamanho, à classe Sobremesa. Ajuste a inicialização da classe para incluir esses novos atributos, possibilitando a criação de um novo item ao cardápio do restaurante.

Atualize o método __str__ conforme necessário para refletir essas mudanças.

Certifique-se de que a classe Sobremesa mantenha a herança do método aplicar_desconto de ItemCardapio.
"""

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.04)
         