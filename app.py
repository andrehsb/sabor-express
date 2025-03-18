from classes.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Pf')
restaurante_pizza = Restaurante('Pizza', 'Massa')
restaurante_praca.receber_avaliacao('bom demais', 10)
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()