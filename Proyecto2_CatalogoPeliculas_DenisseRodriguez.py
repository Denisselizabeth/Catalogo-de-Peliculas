import os
class Peliculas:
    def __init__(self, titulo, genero, duracion, lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self._duracion = duracion
        self.lanzamiento = lanzamiento
    def __str__(self):
        return f"Pelicula:{self.titulo}, Genero:{self.genero}, Duracion:{self._duracion}, Lanzamiento:{self.lanzamiento}"
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
pelicula = Peliculas(titulo= input("Ingrese el título de la película:", 
                     genero= input("Ingrese el géner de la película:",
                     duracion= input("Ingrese la duración de la película:",
                     lanzamiento= input("Ingrese el año de lanzamiento de la película:"
                    )

agregar = pelicula.agregar_pelicula(pelicula)
guardar = pelicula.guardar_pelicula()
eliminar = pelicula.eliminar_pelicula()
listar = pelicula.listar_peliculas()


opcion = int(input("Ingrese una opción: "))
while True:
    print("1. Agregar pelicula")
    print("2. Listar peliculas")
    print("2. Eliminar catalogo de peliculas")
    print("3. Salir")
    if opcion == 1:
        print ({agregar})
        agregar = True
        guardar = True
    elif opcion == 2:
        print ({listar})a
        listar = True
    elif opcion == 3:
        print ({eliminar})
        eliminar = True
    elif opcion == 4:
        print ("¡Hasta Pronto!")
        break
    else:
        print("Ingrese una opcion valida")
