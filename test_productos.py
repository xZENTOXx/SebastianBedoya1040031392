import unittest
from main import Producto_CRUD


class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.crud = Producto_CRUD()

        
        self.crud.guardar_productos([])

        self.producto = {
            "id": 0,
            "nombre": "Mouse",
            "descripcion": "Mouse gamer",
            "precio": 80000,
            "cantidad": 5
        }

    # CREAR
    def test_crear_producto_exitoso(self):
        resultado = self.crud.crear_producto(self.producto)
        self.assertEqual(resultado, "Producto agregado correctamente")

    def test_crear_producto_duplicado(self):
        self.crud.crear_producto(self.producto)
        resultado = self.crud.crear_producto(self.producto)

        self.assertEqual(resultado, "Error: El producto ya existe")

    # LEER
    def test_leer_productos(self):
        self.crud.crear_producto(self.producto)
        productos = self.crud.leer_productos()

        self.assertEqual(len(productos), 1)

    # ACTUALIZAR
    def test_actualizar_producto_exitoso(self):
        self.crud.crear_producto(self.producto)

        resultado = self.crud.actualizar_producto(
            1,
            {"precio": 100000}
        )

        self.assertEqual(resultado, "Producto actualizado")

    def test_actualizar_producto_no_existente(self):
        resultado = self.crud.actualizar_producto(
            99,
            {"precio": 100000}
        )

        self.assertEqual(resultado, "Error: Producto no encontrado")

    # ELIMINAR
    def test_eliminar_producto_exitoso(self):
        self.crud.crear_producto(self.producto)

        resultado = self.crud.eliminar_producto(0)

        self.assertEqual(resultado, "Producto eliminado")

    def test_eliminar_producto_no_existente(self):
        resultado = self.crud.eliminar_producto(99)

        self.assertEqual(resultado, "Error: Producto no encontrado")


if __name__ == "__main__":
    unittest.main()