from typing import Dict
from models.producto import Producto

class ProductoRepository:
    def _init_(self):
        # Diccionario en memoria: id -> Producto
        self._productos: Dict[int, Producto] = {}

    def listar(self):
        return list(self._productos.values())

    def obtener(self, producto_id: int):
        return self._productos.get(producto_id)

    def crear(self, producto: Producto):
        self._productos[producto.id] = producto
        return producto

    def actualizar(self, producto_id: int, producto: Producto):
        if producto_id in self._productos:
            self._productos[producto_id] = producto
            return producto
        return None

    def eliminar(self, producto_id: int):
        return self._productos.pop(producto_id, None)
