import json
import time
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


with open("medallas.json", "r", encoding="utf-8") as archivo:
    medallas = json.load(archivo)

for medalla in medallas[:2]:
    entrenador.agregar_medalla(medalla)


while True:

    print("\n--- MENÚ ---")
    print("1 - Ver Pokédex")
    print("2 - Ver Equipo Principal")
    print("3 - Ver PC")
    print("4 - Ver Medallas")
    print("5 - Capturar nuevo Pokémon")
    print("6 - Ordenar PC")
    print("7 - Buscar Pokémon en Equipo")
    print("8 - Enviar Equipo al Centro Pokémon")
    print("9 - Transferir Pokémon al Profesor Oak")
    print("10 - Deshacer última transferencia")
    print("11 - Desafiar Líder de Gimnasio")
    print("12 - Buscar Pokémon por ID ")
    print("0 - Salir")

    opcion = input("Opción: ")

    if opcion == "1":

        pokedex.mostrar_pokemon()

    elif opcion == "2":

        entrenador.mostrar_equipo()

    elif opcion == "3":

        entrenador.pc.mostrar()

    elif opcion == "4":

        entrenador.mostrar_medallas()

    elif opcion == "5":

        id = int(input("ID del Pokémon: "))

        pokemon = pokedex.buscar_pokemon(id)

        if pokemon:
            entrenador.capturar_pokemon(pokemon)

        else:
            print("No existe ese Pokémon.")

    elif opcion == "6":

        print("1 - Ordenar por nombre")
        print("2 - Ordenar por tipo")
        print("3 - Ordenar por poder")

        op = input("Opción: ")

        if op == "1":
            entrenador.pc.ordenar_nombre()
            entrenador.pc.mostrar()

        elif op == "2":
            entrenador.pc.ordenar_tipo()
            entrenador.pc.mostrar()

        elif op == "3":
            entrenador.pc.ordenar_poder()
            entrenador.pc.mostrar()
        else:
            print("Opcion inválida.")

    elif opcion == "7":

        nombre = input("Nombre: ")

        pokemon = entrenador.buscar_equipo(nombre)

        if pokemon:
            print(pokemon)

        else:
            print("No está en el equipo.")

    elif opcion == "8":

        entrenador.curar_equipo()

    elif opcion == "9":

        nombre = input("Nombre del Pokémon: ")

        entrenador.transferir_oak(nombre)

    elif opcion == "10":

        entrenador.deshacer_transferencia()

    elif opcion == "11":

        entrenador.desafiar_gimnasio()

    elif opcion == "12":

        id = int(input("ID: "))

        pokemon = pokedex.buscar_binaria(id)

        if pokemon:
            print(pokemon)

        else:
            print("No existe ese ID.")

    elif opcion == "0":

        print("Hasta luego.")

        break

    else:

        print("Opción inválida.")
    time.sleep(2)