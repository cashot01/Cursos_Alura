import os
os.system("cls")

restaurantes = [{"nome": "Praça", "categoria": "Japonesa", "ativo":False},
                 {"nome": "Pizza Suprema", "categoria": "Italiana", "ativo": True}, 
                  {"nome": "Cantina", "categoria": "Italiano", "ativo":False}]
# dicionario = [{"nome": "Praça"}]

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

def voltar_ao_menu_principal():
    input("\n Digite uma tecla para voltar ao menu ")
    main()

def opcao_invalida():
    print("opção invalida")
    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system("cls")
    print(texto)
    print()

def cadstrar_novo_resturante():
    exibir_subtitulos("Cadastro de novos restaurantes")
    
    nome_restaurante = input("digite o nome do restaurante: ")
    
    # .append adiciona na lista
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    dados_do_restaurante = {"nome": nome_restaurante,
                            "categoria": categoria,
                            "ativo": False}
    restaurantes.append(dados_do_restaurante)

    print(f"restaurante {nome_restaurante} foi cadastrado com sucesso")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulos("Listando os restaurantes")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"- {nome_restaurante} | {categoria} | {ativo} ")


    voltar_ao_menu_principal()

def escolher_opcao():
    try: # comando q tenta executar 
        opcao_escolhida = int(input("Escolha uma opção: "))
        
        if opcao_escolhida == 1:
            cadstrar_novo_resturante() 
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar Restaurante")
        elif opcao_escolhida ==  4:
            finalizar_app()
        else:
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
