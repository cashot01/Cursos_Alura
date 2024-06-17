import os
os.system("cls")
"""
1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

5 - Crie uma instância da classe e imprima o valor da propriedade titular.

6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

7 - Crie um método de classe para a conta ClienteBanco.
"""
class ContaBancaria:
    def __init__(self, titular = "", saldo = 0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f"Titular: {self._titular} | Saldo {self._saldo} | Status: {self._ativo}"
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def ativo(self):
        return "Ativa" if self._ativo else "Desativada"
    
    @property
    def titular(self):
        return f"{self._titular}"
    
    @property
    def saldo(self):
        return f"{self._saldo}"
    
    @property
    def ativo(self):
        return f"{self._ativo}"


    

conta1 = ContaBancaria("Cauan", 54321)
print(conta1)
print()
conta1.ativar_conta(conta1)
print(conta1)
print()

conta2 = ContaBancaria("Eduardo", 100)
print(conta2)
print(f"Titular conta 2: {conta2.titular}")
print()

class ClienteBanco:
    def __init__(self, nome = "", idade = 0,  endereco = "", cpf = "", profissao = ""):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    
    def __str__(self):
        return f"{self.nome} | {self.idade} | {self.endereco} | {self.cpf} | {self.profissao}"

    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancaria("Cauan", 550)
        return conta
    

cliente1 = ClienteBanco("Cauan", 20, "Rua C", "123.456.789.01", "Medico")
print(cliente1)

conta_cliente1 = ClienteBanco.criar_conta("Cauan", 550)
print(f"Conta de {conta_cliente1.titular} com saldo de {conta_cliente1.saldo}")
