from typing import List
from fastapi import APIRouter, HTTPException
from models.producto import Producto
from repositories.producto_repository import ProductoRepository
from services.producto_service import ProductoService

# Crear instancia del repositorio y del servicio
producto_repository = ProductoRepository()
producto_service = ProductoService(producto_repository)

router = APIRouter(prefix="/farmasync/inventario", tags=["Inventario"])

@router.get("/", response_model=List[Producto], summary="Listar productos")
def listar_productos():
    return producto_service.listar_productos()

@router.get("/{id}", response_model=Producto, summary="Obtener producto por ID")
def obtener_producto(id: int):
    producto = producto_service.obtener_producto(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=Producto, summary="Crear producto")
def crear_producto(producto: Producto):
    try:
        return producto_service.crear_producto(producto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{id}", response_model=Producto, summary="Actualizar producto")
def actualizar_producto(id: int, producto: Producto):
    try:
        updated = producto_service.actualizar_producto(id, producto)
        if not updated:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}", summary="Eliminar producto")
def eliminar_producto(id: int):
    deleted = producto_service.eliminar_producto(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"detalle": "Producto eliminado correctamente"}
