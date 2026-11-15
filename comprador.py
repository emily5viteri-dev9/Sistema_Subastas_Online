
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: comprador.py
# ==========================================

from usuario import Usuario


class Comprador(Usuario):

    def __init__(self, id_usuario, nombre, correo, contrasena, saldo):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.__saldo = saldo

    def obtener_saldo(self):
        return self.__saldo

    def realizar_puja(self, subasta, monto):
        return subasta.registrar_puja(self, monto)

    def mostrar_saldo(self):
        print("Saldo disponible: $", self.__saldo)
