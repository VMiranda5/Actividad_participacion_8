import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError



class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print("4. Salir")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras
    def retirar_libro_de_carrito_de_compras(self):
        isbn_a_eliminar = input('Ingrese el ISBN del libro que va a retirar del carrito: ')
        self.tienda_libros.retirar_item_de_carrito(isbn_a_eliminar)
        print(f'el libro con ISBN {isbn_a_eliminar} ha sido eliminado del carrito')

    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn_a_agregar = input('ingrese el ISBN del libro que va a agregar al carrito: ')
            cantidad = int(input('ingrese la cantidad que va a agregar al carrito: '))
            libro_a_agregar = self.tienda_libros.catalogo[isbn_a_agregar]
            self.tienda_libros.agregar_libro_a_carrito(libro_a_agregar,cantidad)
        except LibroAgotadoError as err:
            print(err)
        except ExistenciasInsuficientesError as err2:
            print(err2)

    # Defina el metodo adicionar_un_libro_a_catalogo       
    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("ingrese el isbn del libro a agregar al carrito")
            titulo = input("ingrese el titulo del libro a agregar al catalogo")
            precio = float(input("ingrese el precio del libro a agregar al catalogo"))
            existencias = int(input("ingrese la cantidad de existencias del libro a agregar al catalogo"))
            libro_a_agregar = self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
        except LibroExistenteError as err3:
            print(err3)




