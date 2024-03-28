import os
os.system("cls")

def exibir_nome_programa():
    print(""" 𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
""")
# para pegar essas letras diferentes no f symbols
    
def finalizar_app(): # def - função em python
    os.system("cls")
    print("finalizando o app")

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1:
        print("Cadastrando Restaurante")
    elif opcao_escolhida == 2:
        print("Listar Restaurante")
    elif opcao_escolhida == 3:
        print("Ativar Restaurante")
    else:
        finalizar_app()


def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
