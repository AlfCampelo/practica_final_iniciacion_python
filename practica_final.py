class Libro:
    # Constructor de la clase Libro
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True # El libro esta disponible


    # Método que añade un libro a la biblioteca
    def agregar(self):
        # Devuelve un diccionario
        return{
            'titulo': self.titulo,
            'autor': self.autor,
            'isbn': self.isbn,
            'disponible': self.disponible
        }

    # Método que presta un libro si se encuentra disponible
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado')
        else:
            print(f'El libro "{self.titulo}", no se encuentra disponible, ya está prestado.')   

    # Método para devolver un libro
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f'El libro "{self.titulo}", ha sido devuelto.')
        else:
            print(f'El libro "{self.titulo}" ya se encontraba disponible.')

    # Imprime la lista de libros
    def mostrar(self):
        estado = 'Disponible' if self.disponible else 'Prestado'
        print(f'Título: {self.titulo}, Autor: {self.autor}, ISNB: {self.isbn}, Estado: {estado}')

    # Busca un libro por su ISBN
    def buscar(self, isbn):
        if self.isbn == isbn:
            self.mostrar()
            return True
        return False


# Gestión del inventario de la biblioteca
class Biblioteca:
    def __init__(self):
        # Crea una lista para almacenar los libros
        self.inventario = []

    # Método para añadir un nuevo libro a la biblioteca

    
    def agregar_libro(self):       
        titulo = input('Introduce el título del libro: ')
        autor = input('Introduce el autor del libro: ')
        # Comprueba que la lista tiene elementos
        if self.inventario:
            existe_isbn = True
            # Comprueba que el ISBN no está repetido
            while existe_isbn:
                isbn = input('Introduce el ISBN del libro: ')
                existe_isbn = False  # Asumimos que el ISBN no existe al inicio
                for libro in self.inventario:
                    if libro.isbn == isbn:
                        print('El ISBN introducido ya existe.')
                        existe_isbn = True  # Si hay coincidencia, existe el ISBN
                        break  # Salimos del bucle for para pedir un nuevo ISBN
        else:
            # Si el inventario está vacío, no hay necesidad de comprobar el ISBN
            isbn = input('Introduce el ISBN del libro: ')
        # Creamos un objeto Libro
        nuevo_libro = Libro(titulo, autor, isbn)
        # Añade el libro al inventario
        self.inventario.append(nuevo_libro)
        print(f'{titulo} añadido con éxito\n')

    # Método para prestar un libro por su ISBN
    def prestar_libro(self):
        isbn = input('Introduce el ISNB del libro a prestar: ')
        existe_libro = False
        # Busca si existe el ISBN buscado, si lo encuentra presta el libro
        for libro in self.inventario:
            if libro.isbn == isbn:
                libro.prestar()
                existe_libro = True
                break
        # Si no encuentra el ISBN imprime un mensaje
        if not existe_libro:
            print(f'El libro con el ISBN {isbn} no ha sido encontrado/n')
    
    # Método que permite devolver un libro
    def devolver_libro(self):
        isbn = input('Introduce el ISBN del libro a devolver: ')
        libro_encontrado = False
        # Busca si existe el ISNB
        for libro in self.inventario:
            if libro.isbn == isbn:
                libro.devolver()
                libro_encontrado = True
                break
        if not libro_encontrado:
            print(f'El libro con ISBN {isbn} no ha sido encontrado/n')

    # Método que muestra el contenido de la biblioteca
    def mostrar_libros(self):
        # Comprueba que la biblioteca no este vacia
        if not self.inventario:
            print('No hay libros en la biblioteca\n')
        else:
            print('Listado de libros en la biblioteca\n')
            for libro in self.inventario:
                libro.mostrar()

            # Línea en blanco al final
            print('\n')

    # Método que busca un libro por su ISBN
    def buscar_libro(self):
        isbn = input('Introduce el ISBN del libro que deseas buscar: ')
        libro_encontrado = False
        for libro in self.inventario:
            if libro.buscar(isbn):
                libro_encontrado = True
                break
        if not libro_encontrado:
            print(f'No existe ningún libro con el ISBN {isbn}\n')

    # Método para salir del programa
    def salir(self):
        print('Saliendo de la gestión de biblioteca.\n')
        exit()
    

# Fin clase Biblioteca

# Programa principal

# Muestra el menú con las diferentes opciones
def mostrar_menu():
    print('Bienvenido al Sistema de Gestión de Biblioteca')
    print('1. Agregar Libro')
    print('2. Prestar Libro')
    print('3. Devolver Libro')
    print('4. Mostrar Libros')
    print('5. Buscar')
    print('6. Salir')

# Función principal para ejecutar el programa
def ejecutar_programa():
    biblioteca = Biblioteca()  # Crear una instancia de la clase Biblioteca

    while True:
        mostrar_menu()  # Mostrar el menú
        try:
            opcion = int(input('Elige una opción: '))
            if opcion == 1:
                biblioteca.agregar_libro()  # Agregar un nuevo libro
            elif opcion == 2:
                biblioteca.prestar_libro()  # Prestar un libro
            elif opcion == 3:
                biblioteca.devolver_libro()  # Devolver un libro
            elif opcion == 4:
                biblioteca.mostrar_libros()  # Mostrar todos los libros
            elif opcion == 5:
                biblioteca.buscar_libro()  # Buscar un libro por ISBN
            elif opcion == 6:
                biblioteca.salir()  # Salir del programa
            else:
                print('Opción no válida. Inténtalo de nuevo.\n')
        except ValueError:
            print('Entrada no válida. Por favor ingresa un número.\n')


# Ejecuta el programa
if __name__ == '__main__':
        ejecutar_programa()
