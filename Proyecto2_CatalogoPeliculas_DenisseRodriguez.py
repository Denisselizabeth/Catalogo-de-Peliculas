import os
class Peliculas:
    def __init__(self, titulo, genero, duracion, lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self._duracion = duracion
        self.lanzamiento = lanzamiento
    def __str__(self):
        return f"Pelicula:{self.titulo}, Genero:{self.genero}, 
        Duracion:{self._duracion}, Lanzamiento:{self.lanzamiento}"
class CatalogoPelicula():
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo
        self.peliculas = []
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar_pelicula()
        return True
    def guardar_pelicula(self):
        with open(self.ruta_archivo, "w") as archivo:
            for pelicula in self.peliculas:
                archivo.write(f"{pelicula.titulo},{pelicula.genero},{pelicula._duracion},{pelicula.lanzamiento}\n")
                archivo.close()
    def eliminar_pelicula(self):
        with open(self.ruta_archivo, "w") as archivo:
            for pelicula in self.peliculas:
                archivo.delete(f"{pelicula.titulo},{pelicula.genero},{pelicula._duracion},{pelicula.lanzamiento}\n")
                archivo.close()   
    def listar_peliculas(self):
        with open(self.ruta_archivo, "r") as archivo:
            for linea in archivo.readlines():
                titulo, genero, duracion, lanzamiento = linea.strip().split(",")
                pelicula = Peliculas(titulo, genero, duracion, lanzamiento)
                self.peliculas.append(pelicula)
                print(pelicula)
                archivo.close()
                return True

while True:
    print("1. Agregar pelicula")
    print("2. Listar peliculas")
    print("2. Eliminar catalogo de peliculas")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        agregar_pelicula()
    elif opcion == 2:
        listar_peliculas()
    elif opcion == 3:
        listar_peliculas()
    elif opcion == 4:
        print ("¡Hasta Pronto!")
        break
    else:
        print("Ingrese una opcion valida")
