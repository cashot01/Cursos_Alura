import os
os.system("cls")
"""
Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
"""
class Pessoa:
    def __init__(self, nome = "", idade = 0, profissao = ""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome} | {self.idade} anos | {self.profissao}"

    @property
    def saudacao(self):
        if self.profissao:
            return f"Olá sou {self.nome},  e trabalho como {self.profissao} "
        else:
            return f"Olá sou {self.nome}"
    
    def aniversario(self):
        self.idade += 1
        
    

pessoa = Pessoa("Cauan", 18, "Estagiario")
pessoa2 = Pessoa("Andrea", 30)
print(pessoa)   
print(pessoa2)   
print()   

pessoa.aniversario()
pessoa2.aniversario()
print(pessoa)
print(pessoa2)
print()

print(pessoa.saudacao)
print()
print(pessoa2.saudacao)


