print("""
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
""")
# para pegar essas letras diferentes no f symbols

print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair\n")

opcao_escolhida = int(input("Escolha uma opção: "))

if opcao_escolhida == 1:
    print("Cadastrando Restaurante")
elif opcao_escolhida == 2:
    print("Listar Restaurante")
elif opcao_escolhida == 3:
    print("Ativar Restaurante")
else:
    print("Encerrando o programa")
