from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_mexicano = Restaurante("mexican food", "mexicano")
restaurante_japones = Restaurante("japa", "japonesa")

restaurante_mexicano.alternar_estado()


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()