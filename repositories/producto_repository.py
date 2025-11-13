from models.producto import Producto
from config.database import producto_collection
from bson import ObjectId

class ProductoRepository:
    def listar(self):
        productos = []
        for p in producto_collection.find():
            p["id"] = str(p["_id"])
            del p["_id"]  # eliminamos el _id interno de Mongo para no duplicar
            productos.append(Producto(**p))
        return productos

    def obtener(self, producto_id: str):
        p = producto_collection.find_one({"_id": ObjectId(producto_id)})
        if p:
            p["id"] = str(p["_id"])
            del p["_id"]
            return Producto(**p)
        return None

    def crear(self, producto: Producto):
        result = producto_collection.insert_one(producto.to_dict())
        producto.id = str(result.inserted_id)
        return producto

    def actualizar(self, producto_id: str, producto: Producto):
        producto_collection.update_one(
            {"_id": ObjectId(producto_id)},
            {"$set": producto.to_dict()}
        )
        return self.obtener(producto_id)

    def eliminar(self, producto_id: str):
        result = producto_collection.delete_one({"_id": ObjectId(producto_id)})
        return result.deleted_count > 0
