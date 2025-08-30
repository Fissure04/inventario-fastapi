from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: Optional[int] = None   # el id puede venir vacío al crearlo, lo asignamos después
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
