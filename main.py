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
    entrenador.capturar_pokemon(pokemon)


pokedex.mostrar_pokemon()

entrenador.mostrar_equipo()

print("\nPOKÉMON EN LA PC")
entrenador.pc.mostrar()



print("\nOrdenado por nombre")
entrenador.pc.ordenar_nombre()
entrenador.pc.mostrar()

print("\nOrdenado por tipo")
entrenador.pc.ordenar_tipo()
entrenador.pc.mostrar()

print("\nOrdenado por poder")
entrenador.pc.ordenar_poder()
entrenador.pc.mostrar()

entrenador.curar_equipo()

entrenador.transferir_oak("Flygon")

entrenador.deshacer_transferencia()


with open("medallas.json", "r", encoding="utf-8") as archivo:
    medallas = json.load(archivo)

for medalla in medallas[:2]:
    entrenador.agregar_medalla(medalla)

entrenador.mostrar_medallas()
entrenador.desafiar_gimnasio()