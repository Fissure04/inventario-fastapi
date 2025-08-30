from fastapi import FastAPI
from controllers import producto_controller

app = FastAPI(
    title="API Productos - Arquitectura Multicapa",
    description="Microservicio de inventario de productos con FastAPI",
    version="1.0.0"
)

# Registrar router de productos
app.include_router(producto_controller.router)
