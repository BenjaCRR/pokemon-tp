class Pokedex:

    def __init__(self):
        self.pokedex = {}

    def agregar_pokemon(self, pokemon):
        self.pokedex[pokemon.id] = pokemon

    def buscar_pokemon(self, id):
        return self.pokedex.get(id)

    def mostrar_pokemon(self):
        print("\nPOKÉDEX NACIONAL")
        for pokemon in self.pokedex.values():
            print(pokemon)