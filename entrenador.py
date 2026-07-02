from collections import deque
import random
import time

class Nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self.inicio = None

    def agregar(self, pokemon):

        nuevo = Nodo(pokemon)
    
        nuevo.siguiente = self.inicio
    
        self.inicio = nuevo

    def eliminar(self, nombre):

        if self.inicio is None:
            return None

        if self.inicio.pokemon.nombre == nombre:
            pokemon = self.inicio.pokemon
            self.inicio = self.inicio.siguiente
            return pokemon

        anterior = self.inicio
        actual = self.inicio.siguiente

        while actual:

            if actual.pokemon.nombre == nombre:
                anterior.siguiente = actual.siguiente
                return actual.pokemon

            anterior = actual
            actual = actual.siguiente

        return None

    def mostrar(self):

        actual = self.inicio

        while actual:
            print(actual.pokemon)
            actual = actual.siguiente

    def a_lista(self):

        lista = []

        actual = self.inicio

        while actual:
            lista.append(actual.pokemon)
            actual = actual.siguiente

        return lista

    def desde_lista(self, lista):

        self.inicio = None

        for pokemon in lista:
            self.agregar(pokemon)


    def ordenar_nombre(self):

        lista = self.a_lista()

        n = len(lista)

        for i in range(n):
            for j in range(n - i - 1):

                if lista[j].nombre < lista[j + 1].nombre:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        self.desde_lista(lista)


    def ordenar_tipo(self):

        lista = self.a_lista()

        for i in range(1, len(lista)):

            actual = lista[i]
            j = i - 1

            while j >= 0 and str(lista[j].tipo) < str(actual.tipo):
                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = actual

        self.desde_lista(lista)


    def quick_sort(self, lista):

        if len(lista) <= 1:
            return lista

        pivote = lista[0]

        mayores = [x for x in lista[1:] if x.poder_combate >= pivote.poder_combate]
        menores = [x for x in lista[1:] if x.poder_combate < pivote.poder_combate]

        return self.quick_sort(mayores) + [pivote] + self.quick_sort(menores)

    def ordenar_poder(self):

        lista = self.quick_sort(self.a_lista())
        lista = lista[::-1]
        self.desde_lista(lista)

class Entrenador:

    def __init__(self):

        self.equipo = []
        self.pc = ListaEnlazada()
        self.centro = deque()
        self.transferidos = []
        self.medallas = set()


    def capturar_pokemon(self, pokemon):

        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
            print(f"{pokemon.nombre} agregado al equipo.")

        else:
            self.pc.agregar(pokemon)
            print(f"{pokemon.nombre} fue enviado a la PC.")

    def mostrar_equipo(self):

        print("\nEQUIPO")

        for pokemon in self.equipo:
            print(pokemon)

    def buscar_equipo(self, nombre):

        for pokemon in self.equipo:

            if pokemon.nombre.lower() == nombre.lower():
                return pokemon

        return None

    def curar_equipo(self):

        for pokemon in self.equipo:
            self.centro.append(pokemon)

        print("\nCurando equipo...")

        while self.centro:

            pokemon = self.centro.popleft()

            print(f"{pokemon.nombre} fue curado.")
            time.sleep(1)

    def transferir_oak(self, nombre):

        pokemon = self.pc.eliminar(nombre)

        if pokemon:

            if len(self.transferidos) == 5:
                self.transferidos.pop(0)

            self.transferidos.append(pokemon)

            print(f"{pokemon.nombre} fue transferido.")

        else:
            print("No existe en la PC.")

    def deshacer_transferencia(self):

        if len(self.transferidos) == 0:
            print("No hay transferencias.")
            return

        pokemon = self.transferidos.pop()

        self.pc.agregar(pokemon)

        print(f"{pokemon.nombre} volvió a la PC.")

    def desafiar_gimnasio(self):

        gimnasios = {
            1: "Medalla Roca",
            2: "Medalla Cascada",
            3: "Medalla Trueno",
            4: "Medalla Arcoiris",
            5: "Medalla Alma",
            6: "Medalla Pantano",
            7: "Medalla Volcan",
            8: "Medalla Tierra"
        }

        opcion = int(input("Elegí un gimnasio (1-8): "))

        if opcion not in gimnasios:
            print("Gimnasio inválido.")
            return

        if random.choice([True, False]):
            print("Luchando...")
            time.sleep(1.67)
            print("¡Ganaste!")

            self.agregar_medalla(gimnasios[opcion])

        else:
            print("Luchando...")
            time.sleep(1.67)
            print("Perdiste.")

    def agregar_medalla(self, medalla):

        if medalla in self.medallas:
            time.sleep(0.5)
            print(f"La medalla '{medalla}' ya fue obtenida.")

        else:
            self.medallas.add(medalla)
            time.sleep(0.5)
            print(f"Se obtuvo la {medalla}.")

    def mostrar_medallas(self):

        print("\nMEDALLAS")

        for medalla in self.medallas:
            print(medalla)
