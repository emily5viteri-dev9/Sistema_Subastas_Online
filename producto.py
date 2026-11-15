
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: producto.py
# ==========================================


class Producto:

    def __init__(self, id_producto, nombre, descripcion, precio_inicial, vendedor):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio_inicial = precio_inicial
        self.__vendedor = vendedor
        self.__disponible = True

    def obtener_id(self):
        return self.__id_producto

    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio_inicial

    def obtener_vendedor(self):
        return self.__vendedor

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_inicial = nuevo_precio
            return True
        return False

    def mostrar_producto(self):
        print("ID del producto:", self.__id_producto)
        print("Nombre:", self.__nombre)
        print("Descripcion:", self.__descripcion)
        print("Precio inicial: $", self.__precio_inicial)
        print("Vendedor:", self.__vendedor.obtener_nombre())
        print("Disponible:", self.__disponible)
