import os
import datetime
os.system("cls")
"""
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
"""
numero = 1
numeros = [1,]
def listar_numeros(numero):
    while numero < 10:
        numero += 1
        numeros.append(numero)
    print(numeros)

listar_numeros(numero)

nomes = []
def lista_4_nomes():
    for i in range(4):
        nome = input("Digite um nome: ")
        nomes.append(nome)
    print(nomes)

lista_4_nomes()

anos = []
def ano_nascimento_E_ano_atual():
   ano_nascimento = int(input("Ano de nascimento:"))
   ano_atual = datetime.date.today().year
   anos.append(ano_nascimento)
   anos.append(ano_atual)
   print(anos)

ano_nascimento_E_ano_atual()
    
   



    