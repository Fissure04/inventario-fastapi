from typing import List, Optional
from models.producto import Producto
from repositories.producto_repository import ProductoRepository

class ProductoService:
    def __init__(self, repository: ProductoRepository):
        self.repository = repository

    def listar_productos(self) -> List[Producto]:
        return self.repository.listar()

    def obtener_producto(self, producto_id: int) -> Optional[Producto]:
        return self.repository.obtener(producto_id)

    def crear_producto(self, producto: Producto) -> Producto:
        # Regla de negocio: stock no puede ser negativo
        if producto.stock < 0:
            raise ValueError("El stock no puede ser negativo")
        return self.repository.crear(producto)

    def actualizar_producto(self, producto_id: int, producto: Producto) -> Optional[Producto]:
        if producto.stock < 0:
            raise ValueError("El stock no puede ser negativo")
        return self.repository.actualizar(producto_id, producto)

    def eliminar_producto(self, producto_id: int) -> Optional[Producto]:
        return self.repository.eliminar(producto_id)
