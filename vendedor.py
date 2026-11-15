
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: vendedor.py
# ==========================================

from usuario import Usuario


class Vendedor(Usuario):

    def __init__(self, id_usuario, nombre, correo, contrasena):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)
        print("Producto agregado correctamente.")

    def listar_productos(self):
        print("Productos publicados:")
        for producto in self.__productos:
            print("-", producto)

    def cantidad_productos(self):
        return len(self.__productos)
