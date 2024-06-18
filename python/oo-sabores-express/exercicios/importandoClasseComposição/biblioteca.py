from livro import Livro

livro_biblioteca = Livro("Livro Biblioteca", "Cauan", 1999)
print(livro_biblioteca)
livro_biblioteca.emprestar_livro()
print(livro_biblioteca)

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")