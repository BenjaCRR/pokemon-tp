import json
from pokemon import Pokemon
from pokedex import Pokedex
from entrenador import Entrenador


pokedex = Pokedex()
entrenador = Entrenador()
with open("pokemon.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

for dato in datos:

    pokemon = Pokemon(
        dato["id"],
        dato["nombre"],
        dato["tipo"],
        dato["poder_combate"]
    )

    pokedex.agregar_pokemon(pokemon)



pokedex.mostrar_pokemon()

print("\nBuscando Pokémon con ID 6...\n")

pokemon = pokedex.buscar_pokemon(195)

if pokemon:
    print(pokemon)
else:
    print("No existe.")

with open("medallas.json", "r", encoding="utf-8") as archivo:
    medallas = json.load(archivo)

for medalla in medallas[:2]:
    entrenador.agregar_medalla(medalla)


print("\nIntentando agregar otra vez la Medalla Roca...\n")

entrenador.agregar_medalla("Medalla Roca")

entrenador.mostrar_medallas()