from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    pass
    # Defina metodo inicializador __init__
    def __init__(self) -> None:
        self.catalogo:dict[str:Libro]={}
        self.carrito:CarroCompras= CarroCompras()
        


    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self,isbn:str, titulo:str, precio:float, existencias:int)->Libro:
        if isbn in self.catalogo:
            raise LibroExistenteError(self.catalogo[isbn])
        else:
            libro = Libro(isbn,titulo,precio, existencias)
            self.catalogo[isbn]=libro
            return libro
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro:Libro,unidades:int):
        if libro.existencias ==0:
            raise LibroAgotadoError(libro)
        if libro.existencias<unidades:
            raise ExistenciasInsuficientesError(libro,unidades)
        else:
            self.carrito.agregar_item(libro,unidades)

    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn:str):
        self.carrito.quitar_item(isbn)