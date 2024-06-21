from abc import ABC, abstractmethod
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    

    @abstractmethod
    #  Isso implica que todas as classes derivadas são obrigadas a seguir essa diretriz; quando dizemos "precisam", é uma exigência real.
    def aplicar_desconto(self):
        # Essa forma de pegar um método e dizer que ele deve se moldar de forma diferente em diferentes classes é o que chamamos na programação de polimorfismo. O mesmo método se adapta para uma classe específica e tem um comportamento diferente através desse método abstrato que criamos na nossa classe principal.
        pass


    