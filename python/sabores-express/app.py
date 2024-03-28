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

def opcao_invalida():
    print("opção invalida")
    input("digite uma tecla para voltar no menu principal ")
    main()

def escolher_opcao():
    try: # comando q tenta executar 
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida:
            case 1:
                print("Cadastrando Restaurante")
            case 2:
                print("Listar Restaurante")
            case 3:
                print("Ativar Restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except: # "else" do try 
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
