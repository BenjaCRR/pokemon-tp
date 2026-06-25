class Entrenador:

    def __init__(self):
        self.medallas = set()

    def agregar_medalla(self, medalla):

        if medalla in self.medallas:
            print(f"La medalla '{medalla}' ya fue obtenida")
        else:
            self.medallas.add(medalla)
            print(f"Se obtuvo la {medalla}.")

    def mostrar_medallas(self):

        print("\nMEDALLAS")

        for medalla in self.medallas:
            print(medalla)