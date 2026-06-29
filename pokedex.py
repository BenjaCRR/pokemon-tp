class Pokedex:

    def __init__(self):
        self.pokedex = {}

    def agregar_pokemon(self, pokemon):
        self.pokedex[pokemon.id] = pokemon

    def buscar_pokemon(self, id):
        return self.pokedex.get(id)

    def mostrar_pokemon(self):

        print("\nPOKÉDEX")

        for pokemon in self.pokedex.values():
            print(pokemon)

    def buscar_binaria(self, id):

        ids = sorted(self.pokedex.keys())

        izquierda = 0
        derecha = len(ids) - 1

        while izquierda <= derecha:

            medio = (izquierda + derecha) // 2

            if ids[medio] == id:
                return self.pokedex[ids[medio]]

            elif ids[medio] < id:
                izquierda = medio + 1

            else:
                derecha = medio - 1

        return None