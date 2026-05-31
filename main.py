import json
import os

ARCHIVO = "productos.json"


class Producto_CRUD:

    def __init__(self):
        if not os.path.exists(ARCHIVO):
            with open(ARCHIVO, "w") as f:
                json.dump([], f)

    def cargar_productos(self):
        with open(ARCHIVO, "r") as f:
            return json.load(f)

    def guardar_productos(self, productos):
        with open(ARCHIVO, "w") as f:
            json.dump(productos, f, indent=4)

   # Acá se CREAN los productos
    def crear_producto(self, producto):
        productos = self.cargar_productos()

        for p in productos:
            if p["id"] == producto["id"]:
                return "Error: El producto ya existe"

        productos.append(producto)
        self.guardar_productos(productos)

        return "Producto agregado correctamente"

    # Acá se LEE los productos
    def leer_productos(self):
        return self.cargar_productos()

    # Acá se actualizan los productos
    def actualizar_producto(self, id_producto, nuevos_datos):
        productos = self.cargar_productos()

        for producto in productos:
            if producto["id"] == id_producto:
                producto.update(nuevos_datos)
                self.guardar_productos(productos)
                return "Producto actualizado"

        return "Error: Producto no encontrado"

    # DELETE
    def eliminar_producto(self, id_producto):
        productos = self.cargar_productos()

        for producto in productos:
            if producto["id"] == id_producto:
                productos.remove(producto)
                self.guardar_productos(productos)
                return "Producto eliminado"

        return "Error: Producto no encontrado"


if __name__ == "__main__":

    crud = Producto_CRUD()

    producto1 = {
        "id": 1,
        "nombre": "Teclado",
        "descripcion": "Teclado mecánico",
        "precio": 150000,
        "cantidad": 50
    }
    producto2 = {
        "id": 2,
        "nombre": "TV",
        "descripcion": "Televisor Samsung TelHorizon 4k",
        "precio": 4999000,
        "cantidad": 90
    }
    producto3 = {
        "id": 3,
        "nombre": "Portatil GX WAR AMD RADEON 6080 GAMERGX",
        "descripcion": "Portatil para gamers con una potente tarjeta gráfica",
        "precio": 9720500,
        "cantidad": 30
    }

    print(crud.crear_producto(producto1))
    print(crud.crear_producto(producto2))
    print(crud.crear_producto(producto3))
    print(crud.leer_productos())