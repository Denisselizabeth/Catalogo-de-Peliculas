import os

class Peliculas:
    def __init__(self, titulo: str, puntuacion: float, lanzamiento: int):
        self.titulo = titulo
        self._puntuacion = puntuacion
        self.lanzamiento = lanzamiento

    def __str__(self):
        return f"Pelicula: {self.titulo}, Puntuacion: {self._puntuacion}, Lanzamiento: {self.lanzamiento}"

class CatalogoPeliculas:
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo
        self.peliculas = []

    def agregar_pelicula(self, pelicula: Peliculas):
        self.peliculas.append(pelicula)
        self.guardar_pelicula()

    def guardar_pelicula(self):
        with open(self.ruta_archivo, "w") as archivo:
            for pelicula in self.peliculas:
                archivo.write(f"{pelicula.titulo},{pelicula._puntuacion},{pelicula.lanzamiento}\n")

    def eliminar_catalogo(self):
        self.peliculas = []
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)

    def listar_peliculas(self):
        if not os.path.exists(self.ruta_archivo):
            print("No hay películas en el catálogo.")
            return
        with open(self.ruta_archivo, "r") as archivo:
            self.peliculas = []
            for linea in archivo.readlines():
                titulo, puntuacion, lanzamiento = linea.strip().split(",")
                pelicula = Peliculas(titulo, float(puntuacion), int(lanzamiento))
                self.peliculas.append(pelicula)
                print(pelicula)

nombre_catalogo = input("Ingrese el nombre del genero del catalogo de peliculas: ")
ruta_archivo = "/Users/denisselizabeth/Dropbox/DENISSE/Denisse/ADA/Proyecto 2/" + nombre_catalogo + ".txt"
catalogo = CatalogoPeliculas(nombre_catalogo, ruta_archivo)

while True:
    print("Menu de Opciones:")
    print("1. Agregar pelicula")
    print("2. Listar peliculas")
    print("3. Eliminar catalogo de peliculas")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        titulo = input("Ingrese el título de la película: ")
        puntuacion = float(input("Puntúe la película de 1 a 5 estrellas. Solo ingrese números: "))
        lanzamiento = int(input("Ingrese el año de lanzamiento de la película. Solo ingrese números: "))
        pelicula = Peliculas(titulo, puntuacion, lanzamiento)
        catalogo.agregar_pelicula(pelicula)
    elif opcion == 2:
        catalogo.listar_peliculas()
    elif opcion == 3:
        catalogo.eliminar_catalogo()
    elif opcion == 4:
        print("¡Hasta Pronto!")
        break
    else:
        print("Ingrese una opción válida")
