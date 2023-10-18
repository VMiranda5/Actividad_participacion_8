from tiendalibros.modelo.item_compra import ItemCompra

from tiendalibros.modelo.libro import Libro

class CarroCompras:
    pass
    # Defina metodo inicializador __init__(self)
    def __init__(self) -> None:
        self.items:list[ItemCompra]=[]

    # Defina el metodo agregar_item
    def agregar_item(self, libro:Libro, cantidad:int)->ItemCompra:
        item_creado:ItemCompra=ItemCompra(libro,cantidad)
        self.items.append(item_creado)
        return item_creado

    # Defina el metodo calcular_total
    def calcular_total(self):
        total=0
        for i in self.items:
            total+=i.calcular_subtotal()
        return total

    # Defina el metodo quitar_item
    def quitar_item(self, isbn:str):
        temp_list = [i for i in self.items if i.libro.isbn!=isbn]
        self.items = temp_list