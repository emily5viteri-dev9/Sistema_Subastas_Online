
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: usuario.py
# ==========================================

class Usuario:

    def __init__(self, id_usuario, nombre, correo, contrasena):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena
        self.__activo = True

    def obtener_id(self):
        return self.__id_usuario

    def obtener_nombre(self):
        return self.__nombre

    def obtener_correo(self):
        return self.__correo

    def esta_activo(self):
        return self.__activo

    def cambiar_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self.__nombre = nuevo_nombre
            return True
        return False

    def cambiar_correo(self, nuevo_correo):
        if "@" in nuevo_correo:
            self.__correo = nuevo_correo
            return True
        return False

    def desactivar_cuenta(self):
        self.__activo = False

    def mostrar_informacion(self):
        print("ID:", self.__id_usuario)
        print("Nombre:", self.__nombre)
        print("Correo:", self.__correo)
        print("Estado:", "Activo" if self.__activo else "Inactivo")
