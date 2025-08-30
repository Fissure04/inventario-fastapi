# Microservicio de Inventario - FastAPI

Este proyecto es un microservicio de Inventario desarrollado en **Python** usando **FastAPI** y documentado automáticamente con **Swagger (OpenAPI)**.  

## Características
- CRUD de productos (crear, listar, obtener, actualizar, eliminar).
- Arquitectura multicapa: Controller → Service → Repository → Model.
- Documentación automática con Swagger UI.

## Estructura
inventario/
│── main.py
│── controllers/
│ └── producto_controller.py
│── services/
│ └── producto_service.py
│── repositories/
│ └── producto_repository.py
│── models/
│ └── producto.py

## Cómo ejecutar
1. Instala dependencias:
   ```consola
   pip install fastapi uvicorn
   
2. Corre el servidor:
uvicorn main:app --reload

3.Abre en navegador:
  Swagger UI → http://127.0.0.1:8000/docs
  Redoc → http://127.0.0.1:8000/redoc

## Endpoints principales

GET /productos → listar productos

GET /productos/{id} → obtener producto por ID

POST /productos → crear producto

PUT /productos/{id} → actualizar producto

DELETE /productos/{id} → eliminar producto
