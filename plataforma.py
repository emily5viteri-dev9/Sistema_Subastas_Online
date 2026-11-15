
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: plataforma.py
# ==========================================


class Plataforma:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__usuarios = []
        self.__productos = []
        self.__subastas = []

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print("Usuario registrado correctamente.")

    def publicar_producto(self, producto):
        self.__productos.append(producto)
        print("Producto publicado en la plataforma.")

    def crear_subasta(self, subasta):
        self.__subastas.append(subasta)
        print("Subasta creada correctamente.")

    def listar_usuarios(self):
        print("\nUSUARIOS REGISTRADOS:")
        for usuario in self.__usuarios:
            print("-", usuario.obtener_nombre())

    def listar_productos(self):
        print("\nPRODUCTOS DISPONIBLES:")
        for producto in self.__productos:
            print("-", producto.obtener_nombre())

    def listar_subastas(self):
        print("\nSUBASTAS DE LA PLATAFORMA:")
        for subasta in self.__subastas:
            print("-", subasta.obtener_producto().obtener_nombre())

    def mostrar_informacion(self):
        print("\nPLATAFORMA:", self.__nombre)
        print("Total de usuarios:", len(self.__usuarios))
        print("Total de productos:", len(self.__productos))
        print("Total de subastas:", len(self.__subastas))
