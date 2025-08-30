from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    cantidad: int
    precio: float
