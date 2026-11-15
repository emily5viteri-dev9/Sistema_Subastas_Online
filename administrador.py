
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: administrador.py
# ==========================================

from usuario import Usuario


class Administrador(Usuario):

    def __init__(self, id_usuario, nombre, correo, contrasena):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.__permisos = [
            "Gestionar usuarios",
            "Supervisar subastas"
        ]

    def obtener_permisos(self):
        return self.__permisos

    def gestionar_usuario(self, usuario):
        usuario.desactivar_cuenta()
        print("La cuenta del usuario ha sido desactivada.")

    def supervisar_subastas(self):
        print("El administrador esta supervisando las subastas.")

    def mostrar_permisos(self):
        print("Permisos del administrador:")
        for permiso in self.__permisos:
            print("-", permiso)
