import os
os.system("cls")
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
# class = classe 
class Restaurante:
          
    restaurantes = []

    # atributos da classe
    def __init__(self, nome, categoria): # construtor 
      # self tbm pode ser this (do java)
      self._nome = nome.title()
      self._categoria = categoria.upper()
      self._ativo = False
      # _ativo atributo protegido
      self._avaliacao = []
      self._cardapio = []
      Restaurante.restaurantes.append(self)
    
    # metodo especiais tem __exemplo__ (underline underline antes e depois)
    def __str__(self):
      """
      O método __str__ é um método especial que pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto, mostraremos determinada informação.
      Então, em vez de mostrar a representação do endereço de memória, ele mostrará o que decidirmos.
      """
      return f"{self._nome} | {self._categoria} "
    
    @classmethod
    def listar_restaurantes(cls):
       print(f"{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}")
       for restaurante in cls.restaurantes:
          print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property # modificar aquele atributo que vai ser lido
    def ativo(self):
       return "⌧" if self._ativo else "☐"
    
    def alternar_estado(self):
       self._ativo = not self._ativo

   

    def receber_avaliacao(self, cliente, nota):
       if 0 < nota <= 5:
         avaliacao = Avaliacao(cliente, nota)
         self._avaliacao.append(avaliacao)

    @property  
    def media_avaliacoes(self):
       if not self._avaliacao:
          return "-"
       soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
       quantidade_notas = len(self._avaliacao)
       media =round( soma_das_notas / quantidade_notas, 1)
       # round arredonda com uma casa decimal nesse caso
       return media

    def adicionar_no_cardapio(self, item):
       if isinstance(item, ItemCardapio):
          self._cardapio.append(item)

    @property
    def exibir_cardapio(self): 
       print(f"Caradapio do restaurante {self._nome} \n")
       for i, item in enumerate(self._cardapio, start=1):
          if hasattr(item, "descricao"):
             mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}"
             print(mensagem_prato)
          else:
             mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}"
             print(mensagem_bebida)
            
             
      
      
       
          
      
    

# restaurante_praca = Restaurante("praça", "Gourmet")
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante("pizza express", "Italiana")

# Restaurante.listar_restaurantes()

# print(vars(restaurante_praca))

"""
 objeto dir() já possui uma série de informações, como __classe__. Sempre que temos esse __ (underline, underline), significa que é um método especial que toda classe em Python possui.

 exemplo: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ativo', 'categoria', 'nome']

  o dir() mostrará tudo: os atributos, métodos e propriedades de um objeto. 

  Quando o substituímos por vars(), queremos um dicionário desses atributos e métodos.

  exemplo: {'nome': 'Praça', 'categoria': 'Gourmet'}
"""