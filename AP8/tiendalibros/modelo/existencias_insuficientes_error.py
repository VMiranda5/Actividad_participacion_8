from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro: Libro,cantidad_a_comprar:int):
        super().__init__(libro)
        self.cantidad_a_comprar:int=cantidad_a_comprar


    def __str__(self) -> str:
        return f"El libro con título {self.libro.titulo} y ISBN: {self.libro.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}"

    # Defina metodo inicializador

    # Defina metodo espcial
