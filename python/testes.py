"""
07 Funções e fluxos no universo do Streaming

Imagine que você está desenvolvendo um projeto para um serviço de streaming de música. Sua tarefa é melhorar o algoritmo de recomendação de músicas, garantindo que os usuários recebam sugestões mais precisas com base em seus gêneros favoritos. Para isso, você precisa criar uma função em Python que classifique as sugestões de músicas utilizando estruturas condicionais if, else e elif.

No processo de desenvolvimento, você escreveu a seguinte função para classificar uma música como 'recomendada', 'neutra' ou 'não recomendada' com base na preferência do gênero musical do usuário:



Após analisar a função, determine qual será a saída se o gênero favorito do usuário for 'Rock' e o gênero da música for 'Pop'.
"""
# def classificar_musica(genero_favorito, genero_musica):
#     if genero_favorito == genero_musica:
#         return 'recomendada'
#     elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
#         return 'neutra'
#     else:
#         return 'não recomendada'

# resultado = classificar_musica('Rock', 'Pop')
# print(resultado)

"""
8 Compreendo Condicionais

Imagine que você está desenvolvendo um aplicativo chamado Fokus, inspirado na técnica Pomodoro de gerenciamento de tempo. O objetivo do Fokus é ajudar as pessoas a se concentrarem em suas tarefas usando períodos de trabalho focados intercalados com breves intervalos. Uma característica importante do seu aplicativo é permitir que o usuário escolha o tempo de foco e o tempo de pausa.

Você precisa escrever uma função que pergunte ao usuário quanto tempo deseja configurar para o período de foco e, em seguida, use condicionais para verificar se o tempo inserido está dentro de um intervalo aceitável (por exemplo, entre 25 e 45 minutos).

Qual das seguintes implementações da função configurar_tempo_foco está correta e segue as melhores práticas aprendidas no curso?

"""
# def configurar_tempo_foco():
#     import os
#     os.system("cls")
#     tempo = int(input("digite tempo para foco (25-45min): "))
#     if 25 <= tempo <= 45:
#         print("tempo aceitavel")
#     else:
#         print("tempo invalido")

# def main():
#     configurar_tempo_foco()

# if __name__ == "__main__":
#     main()