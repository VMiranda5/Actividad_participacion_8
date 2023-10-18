from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    # Defina metodo inicializador
    def __init__(self, libro: Libro):
        super().__init__(libro)
    # Defina metodo especial
    def __str__(self) -> str:
        return f"El libro con título {self.libro.titulo} y ISBN: {self.libro.isbn} ya existe en el catálogo"
