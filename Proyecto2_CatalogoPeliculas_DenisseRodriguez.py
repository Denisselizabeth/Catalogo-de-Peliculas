import os
class Peliculas:
    def __init__(self, titulo, genero, duracion, lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self._duracion = duracion
        self.lanzamiento = lanzamiento
    def __str__(self):
        return f"Pelicula:{self.titulo}, Genero:{self.genero}, Duracion:{self._duracion}, Lanzamiento:{self.lanzamiento}"
class CatalogoPeliculas:
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo
        self.peliculas = []
    def agregar_pelicula(self, nombre, pelicula):
        self.peliculas.append(pelicula)
        self.guardar_pelicula(nombre)
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

nombre_catalogo = input("Ingrese el nombre del genero del catalogo de peliculas: ")
ruta_archivo = "/Users/denisselizabeth/Dropbox/DENISSE/Denisse/ADA/Proyecto 2"+nombre_catalogo
catalogo=CatalogoPeliculas(nombre_catalogo,ruta_archivo)

while True:
    print("Menu de Opciones:")
    print("1. Agregar pelicula")
    print("2. Listar peliculas")
    print("2. Eliminar catalogo de peliculas")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        pelicula = Peliculas(
                    titulo= input("Ingrese el título de la película:"), 
                    genero= input("Ingrese el género de la película:"),
                    duracion= input("Ingrese la duración de la película:"),
                    lanzamiento= input("Ingrese el año de lanzamiento de la película:")
                    )
        pelicula.agregar_pelicula(titulo, genero, duracion, lanzamiento)
        catalogo.guardar_pelicula(pelicula)
    elif opcion == 2:
        print ({listar})
        catalogo.listar_peliculas()
    elif opcion == 3:
        print ({eliminar})
        catalogo.eliminar_pelicula()
    elif opcion == 4:
        print ("¡Hasta Pronto!")
        break
    else:
        print("Ingrese una opcion valida")
