from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante("praça", "Gourmet")
bebida_suco = Bebida("Suco de melância", 5.0, "grande")
bebida_suco.aplicar_desconto()

prato_paozinho = Prato("Paozinho", 2.00, "Melhor pão da cidade")
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

print()
sobremesa_pudim = Sobremesa("Pudim", 5.5,"Pudim de leite com canela", "Doce", "Medio")
sobremesa_pudim.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)



def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()