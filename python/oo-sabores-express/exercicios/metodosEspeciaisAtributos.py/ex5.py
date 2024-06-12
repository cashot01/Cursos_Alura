import os
os.system("cls")
"""
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
"""
class Cliente:
    clientes = []

    def __init__(self, nome, telefone, endereco, email):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        Cliente.clientes.append(self)
    
    def __str__(self):
        return f"{self.nome} | {self.telefone} | {self.endereco}"
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f"{cliente.nome} | {cliente.telefone} | {cliente.endereco}")

cliente1 = Cliente("Cauan", 987654321, "Rua Passos 543", "cauan@gmail.com")
cliente1 = Cliente("Andrea", 123456789,  "Rua Aranega 395", "andrea@gmail.com")

Cliente.listar_clientes()