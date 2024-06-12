import os
os.system("cls")
# class Musica:
#     nome = ""
#     artista = ""
#     duracao = int

# musica1 = Musica()
# musica1.nome = "Superman"
# musica1.artista = "Emminem"
# musica1.duracao = 245

# print(vars(musica1))

"""
Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.
"""
class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f"{self.nome} | {self.artista} | {self.duracao}"
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.duracao}")

musica1 = Musica("Superman", "Eminem", 345)
musica2 = Musica("Belive", "Imagine Dragrons", 123)

Musica.listar_musicas()