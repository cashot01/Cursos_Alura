from abc import ABC, abstractmethod
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    

    @abstractmethod
    #  Isso implica que todas as classes derivadas são obrigadas a seguir essa diretriz; quando dizemos "precisam", é uma exigência real.
    def aplicar_desconto(self):
        pass


    