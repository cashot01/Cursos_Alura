from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    # classe prato vai herdar a classe ItemCardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        # super permite acessar informações de outra classe
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)