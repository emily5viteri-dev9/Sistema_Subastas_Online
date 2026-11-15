
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: puja.py
# ==========================================


class Puja:

    def __init__(self, id_puja, comprador, monto):
        self.__id_puja = id_puja
        self.__comprador = comprador
        self.__monto = monto

    def obtener_id(self):
        return self.__id_puja

    def obtener_comprador(self):
        return self.__comprador

    def obtener_monto(self):
        return self.__monto

    def mostrar_puja(self):
        print("ID de puja:", self.__id_puja)
        print("Comprador:", self.__comprador.obtener_nombre())
        print("Monto ofertado: $", self.__monto)
