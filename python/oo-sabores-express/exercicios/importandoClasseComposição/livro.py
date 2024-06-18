import os
os.system("cls")

"""
1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

2. Na classe Livro, adicione um método especial **str** que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

4. Adicione um método estático chamado `verificar_disponibilidade` à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

7. No arquivo biblioteca.py, utilize o método estático `verificar_disponibilidade` para obter a lista de livros disponíveis publicados em um ano específico.

8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
"""

class Livro:
    def __init__(self, titulo = "", autor = "", ano_publicado = 0):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} | {self.autor} | {self.ano_publicado} | {self.disponivel}"
    
    
    def emprestar_livro(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicado == ano and livro.disponivel]
        return livros_disponiveis
        

    
livro1 = Livro("Teste", "Cashot01", 2010)
livro2 = Livro("Teste 2", "Cashot01", 2015)
print(livro1)
print()
print(livro2)
print()

livro3 = Livro("Livro3", "Ande", 1986)
print(livro3)
livro3.emprestar_livro()
print(livro3)

Livro.livros = [livro1, livro2, livro3]