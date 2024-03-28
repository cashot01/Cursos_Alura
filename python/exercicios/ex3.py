"""
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
"""
nome = str(input("digite seu nome de usuario (somente letras): "))
senha = str(input("senha (somente letras): "))

if type(nome) and type(senha) != str:
    print(f"usuario {nome} e senha {senha} invalidos ")
else:
    print(f"usuario {nome} e senha {senha} aceitos")